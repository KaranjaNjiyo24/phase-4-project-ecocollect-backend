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
    
    print("Creating sample PickupRequests...")
    # Garbage descriptions and locations
    garbage_descriptions = [
        "Plastic Bottles",
        "Biodegradable Waste",
        "E-Waste",
        "Glass Containers",
        "Metal Cans",
        "Textiles",
        "Mixed Waste",
        "Cardboard Boxes",
        "Paper Waste",
        "Organic Waste"
    ]

    locations = [
        "Uthiru",
        "Parklands",
        "Westlands",
        "Karen",
        "Eastleigh",
        "Lang'ata",
        "Gikambura",
        "Gacharage",
        "Mathare",
        "Lavington"
    ]

    # Create PickupRequests
    pickup_requests = []
    residents = [user for user in users if user.role == "resident"]
    
    for i in range(10):
        resident = residents[i % len(residents)]
        pr = PickupRequest(
            description=garbage_descriptions[i],
            location=locations[i],
            user_id=resident.id
        )
        pickup_requests.append(pr)
        db.session.add(pr)

    db.session.commit()

    print("Creating sample Assignments...")
    # Create assignments for pickup requests
    collectors = [user for user in users if user.role == "collector"]
    statuses = ["pending", "in-progress", "completed"]
    
    for i, pr in enumerate(pickup_requests):
        collector = collectors[i % len(collectors)]
        status = statuses[i % len(statuses)]
        scheduled_date = datetime.utcnow() + timedelta(days=random.randint(1, 10))
        
        assignment = Assignment(
            status=status,
            scheduled_date=scheduled_date,
            collector_id=collector.id,
            pickup_request_id=pr.id
        )
        db.session.add(assignment)

    db.session.commit()

    print("Database seeded successfully!")

if __name__ == "__main__":
    # Create an application context
    with app.app_context():
        seed_data()