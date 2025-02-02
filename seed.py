from app import app
from models import db, User, PickupRequest, Assignment
from datetime import datetime, timedelta
import random

def seed_data():

    print("Clearing existing data...")

    # Delete from tables in dependency order
    Assignment.query.delete()
    PickupRequest.query.delete()
    User.query.delete()

    db.session.commit()

    print("Creating sample Users...")
    # Create some sample Users (5 residents, 5 collectors)
    usernames = [
        "Mbogi_Sunshine",
        "KenyanExplorer",
        "NairobiKanairo",
        "Safari_Adventurer",
        "LakesideQueen",
        "Swahili_Soul",
        "MaasaiShuka",
        "Jambo_Joy",
        "Kayole_Knight",
        "Coastal_Mahamri"
    ]

    users = []
    for i, username in enumerate(usernames):
        role = "resident" if i < 5 else "collector"
        user = User(username=username, role=role)
        users.append(user)
        db.session.add(user)
    
    db.session.commit()
    db.session.add_all([user1, user2, user3])
    db.session.commit()

if __name__ == "__main__":
    # Create an application context
    with app.app_context():
        seed_data()