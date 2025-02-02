from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    role = db.Column(db.String, nullable=False, default="resident")
    
    # One-to-many: A resident can have multiple PickupRequests.
    pickup_requests = db.relationship('PickupRequest', backref='resident', lazy=True)
    # Many-to-many (via Assignment): A collector can have multiple Assignments.
    assignments = db.relationship('Assignment', backref='collector', lazy=True)

    def __repr__(self):
        return f"<User {self.id} username={self.username} role={self.role}>"