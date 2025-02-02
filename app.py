#!/usr/bin/env python3
import os
from flask import Flask, request
from flask_restful import Resource, Api, abort
from flask_migrate import Migrate
from models import db, User, PickupRequest, Assignment
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# SQLite database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'ecocollect.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration modules
db.init_app(app)
migrate = Migrate(app, db)

# Initialize Flask-RESTful API
api = Api(app)

## Defining Resource Classes
class IndexResource(Resource):
    def get(self):
        return {"message": "Welcome to EcoCollect API!"}, 200
    
# User Resources
class UsersListResource(Resource):
    def get(self):
        users = User.query.all()
        return [{"id": user.id, "username": user.username, "role": user.role} for user in users], 200

    def post(self):
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400

        username = data.get("username")
        role = data.get("role", "resident")  # Defaults to "resident" if not provided

        if not username:
            return {"error": "Username is required"}, 400

        new_user = User(username=username, role=role)
        db.session.add(new_user)
        db.session.commit()
        return {"id": new_user.id, "username": new_user.username, "role": new_user.role}, 201
    
class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            abort(404, message=f"User with id {user_id} not found")
        return {"id": user.id, "username": user.username, "role": user.role}, 200

    def put(self, user_id):
        user = User.query.get(user_id)
        if not user:
            abort(404, message=f"User with id {user_id} not found")
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400

        user.username = data.get("username", user.username)
        user.role = data.get("role", user.role)
        db.session.commit()
        return {"id": user.id, "username": user.username, "role": user.role}, 200

    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            abort(404, message=f"User with id {user_id} not found")
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User with id {user_id} deleted."}, 200

# Pickup Request resource
class PickupRequestsListResource(Resource):
    def get(self):
        pickup_requests = PickupRequest.query.all()
        result = []
        for pr in pickup_requests:
            result.append({
                "id": pr.id,
                "description": pr.description,
                "location": pr.location,
                "resident_id": pr.user_id
            })
        return result, 200

    def post(self):
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400

        description = data.get("description")
        location = data.get("location")
        user_id = data.get("user_id")

        if not (description and location and user_id):
            return {"error": "description, location, and user_id are required"}, 400

        new_pr = PickupRequest(description=description, location=location, user_id=user_id)
        db.session.add(new_pr)
        db.session.commit()
        return {
            "id": new_pr.id,
            "description": new_pr.description,
            "location": new_pr.location,
            "resident_id": new_pr.user_id
        }, 201

class PickupRequestResource(Resource):
    def get(self, pr_id):
        pr = PickupRequest.query.get(pr_id)
        if not pr:
            abort(404, message=f"PickupRequest with id {pr_id} not found")
        return {
            "id": pr.id,
            "description": pr.description,
            "location": pr.location,
            "resident_id": pr.user_id
        }, 200

    def put(self, pr_id):
        pr = PickupRequest.query.get(pr_id)
        if not pr:
            abort(404, message=f"PickupRequest with id {pr_id} not found")
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400

        pr.description = data.get("description", pr.description)
        pr.location = data.get("location", pr.location)
        pr.user_id = data.get("user_id", pr.user_id)
        db.session.commit()
        return {
            "id": pr.id,
            "description": pr.description,
            "location": pr.location,
            "resident_id": pr.user_id
        }, 200

    def delete(self, pr_id):
        pr = PickupRequest.query.get(pr_id)
        if not pr:
            abort(404, message=f"PickupRequest with id {pr_id} not found")
        db.session.delete(pr)
        db.session.commit()
        return {"message": f"PickupRequest with id {pr_id} deleted."}, 200
    
# Assignment resource
class AssignmentsListResource(Resource):
    def get(self):
        assignments = Assignment.query.all()
        result = []
        for assign in assignments:
            result.append({
                "id": assign.id,
                "status": assign.status,
                "scheduled_date": assign.scheduled_date,
                "collector_id": assign.collector_id,
                "pickup_request_id": assign.pickup_request_id
            })
        return result, 200

    def post(self):
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400

        collector_id = data.get("collector_id")
        pickup_request_id = data.get("pickup_request_id")
        status = data.get("status", "pending")
        scheduled_date = data.get("scheduled_date")

        if not (collector_id and pickup_request_id):
            return {"error": "collector_id and pickup_request_id are required"}, 400

        new_assignment = Assignment(
            collector_id=collector_id,
            pickup_request_id=pickup_request_id,
            status=status,
            scheduled_date=scheduled_date
        )
        db.session.add(new_assignment)
        db.session.commit()
        return {
            "id": new_assignment.id,
            "status": new_assignment.status,
            "scheduled_date": new_assignment.scheduled_date,
            "collector_id": new_assignment.collector_id,
            "pickup_request_id": new_assignment.pickup_request_id
        }, 201

class AssignmentResource(Resource):
    def get(self, assign_id):
        assign = Assignment.query.get(assign_id)
        if not assign:
            abort(404, message=f"Assignment with id {assign_id} not found")
        return {
            "id": assign.id,
            "status": assign.status,
            "scheduled_date": assign.scheduled_date,
            "collector_id": assign.collector_id,
            "pickup_request_id": assign.pickup_request_id
        }, 200

    def put(self, assign_id):
        assign = Assignment.query.get(assign_id)
        if not assign:
            abort(404, message=f"Assignment with id {assign_id} not found")
        data = request.get_json()
        if not data:
            return {"error": "No input data provided"}, 400

        assign.status = data.get("status", assign.status)
        assign.scheduled_date = data.get("scheduled_date", assign.scheduled_date)
        db.session.commit()
        return {
            "id": assign.id,
            "status": assign.status,
            "scheduled_date": assign.scheduled_date,
            "collector_id": assign.collector_id,
            "pickup_request_id": assign.pickup_request_id
        }, 200

    def delete(self, assign_id):
        assign = Assignment.query.get(assign_id)
        if not assign:
            abort(404, message=f"Assignment with id {assign_id} not found")
        db.session.delete(assign)
        db.session.commit()
        return {"message": f"Assignment with id {assign_id} deleted."}, 200
    
# Adding each resource to the API with their endpoints
api.add_resource(IndexResource, '/')
api.add_resource(UsersListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(PickupRequestsListResource, '/pickup_requests')
api.add_resource(PickupRequestResource, '/pickup_requests/<int:pr_id>')
api.add_resource(AssignmentsListResource, '/assignments')
api.add_resource(AssignmentResource, '/assignments/<int:assign_id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
