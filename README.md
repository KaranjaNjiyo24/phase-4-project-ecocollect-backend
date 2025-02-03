# EcoCollect Backend API

Welcome to the EcoCollect Backend API—a robust, RESTful API built with Flask, Flask-RESTful, and Flask-JWT-Extended(coming soon), using PostgeSQL as its database. This API powers the EcoCollect application, a solution for improving waste management efficiency in urban Nairobi.

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The EcoCollect Backend API provides endpoints for:

- **User Management:** Create, update, retrieve, and delete users.
- **Pickup Requests:** Manage waste pickup requests submitted by residents.
- **Assignments:** Handle the assignment of collectors to pickup requests.

This API is designed to work seamlessly with a React frontend, and it is deployed on Render for high availability and scalability.

---

## Features

- **RESTful API:** Clean and modular endpoint design using Flask-RESTful.
- **Authentication:** Secure user registration and login with JWT.
- **Database:** SQLite for development with Flask-Migrate for database migrations.
- **CORS Enabled:** Easily integrates with a frontend application.
- **Deployed on Render:** Live on Render for effortless deployment.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pipenv (Python package installer)
- Git (optional)

### Setup Steps

1. **Clone the Repository**

   ```bash
   git clone git@github.com:KaranjaNjiyo24/phase-4-project-ecocollect-backend.git
   cd phase-4-project-ecocollect-backend
Create and Activate a Virtual Environment

```bash
Copy
pipenv install
pipenv shell
```
Install Dependencies


```bash
pipenv install flask flask_sqlalchemy flask_migrate flask_restful flask_jwt_extended flask-cors
```
Initialize the Database


```bash
export FLASK_APP=app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
Usage
To start the development server, run:

```bash
python app.py
```
The API will be available at [Eco-collect](https://phase-4-project-ecocollect-backend-1.onrender.com/).

## API Endpoints
Public Endpoints
- GET /
  Returns a welcome message.

- GET /users
  Retrieve a list of users.

- GET /users/<user_id>
  Retrieve a specific user.

- PUT /users/<user_id>
  Update a user.

- DELETE /users/<user_id>
  Delete a user.

- GET /pickup_requests
  Retrieve all pickup requests.

- POST /pickup_requests
  Create a new pickup request.

- GET /assignments
  Retrieve all assignments.

- POST /assignments
  Create a new assignment.
---

For additional endpoints and details, please refer to the source code.


```makefile
Deployment
```
This backend is deployed on Render. You can access the live API at:

[https://ecocollect-backend.onrender.com](https://phase-4-project-ecocollect-backend-1.onrender.com/)

## Frontend Repo
[Ecocollect-Frontend](https://github.com/KaranjaNjiyo24/phase-4-project-ecocollect-frontend/)

---
## Coming soon 
- Authentication
The API to use JWT for authentication.

## Contributing
Contributions are welcome! Please follow these steps:

- Fork the repository.
- Create a new branch (git checkout -b feature/YourFeature).
- Commit your changes (git commit -m 'Add new feature').
- Push to the branch (git push origin feature/YourFeature).
- Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
