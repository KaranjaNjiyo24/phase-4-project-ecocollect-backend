from app import app
from models import db, User, PickupRequest, Assignment

def seed_data():

    print("Clearing existing data...")

    # Delete from tables in dependency order
    Assignment.query.delete()
    PickupRequest.query.delete()
    User.query.delete()

    db.session.commit()

if __name__ == "__main__":
    # Create an application context
    with app.app_context():
        seed_data()