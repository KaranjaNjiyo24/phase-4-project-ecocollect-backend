from app import app
from models import db, User, PickupRequest, Assignment



if __name__ == "__main__":
    # Create an application context
    with app.app_context():
        seed_data()