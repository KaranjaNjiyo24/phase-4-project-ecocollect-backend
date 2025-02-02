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


if __name__ == '__main__':
    app.run(port=5555, debug=True)
