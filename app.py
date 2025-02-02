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
        role = data.get("role", "resident")  # Default to "resident" if not provided

        if not username:
            return {"error": "Username is required"}, 400

        new_user = User(username=username, role=role)
        db.session.add(new_user)
        db.session.commit()
        return {"id": new_user.id, "username": new_user.username, "role": new_user.role}, 201


if __name__ == '__main__':
    app.run(port=5555, debug=True)
