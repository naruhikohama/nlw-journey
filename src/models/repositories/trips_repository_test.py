import uuid
from datetime import datetime, timedelta
from .trips_repository import TripRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()   
trip_id = str(uuid.uuid4())

def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripRepository(conn)

    trips_infos = {
        "id": trip_id,
        "destination": "São Paulo",
        "start_date": datetime.strptime('02-01-2024', '%d-%m-%Y'),
        "end_date": datetime.strptime('02-02-2024', '%d-%m-%Y') + timedelta(days=5),
        "owner_name": "Lucas",
        "owner_email": "lucas@email.com"
    }

    trips_repository.create_trip(trips_infos)

def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trips_repository = TripRepository(conn)

    trip = trips_repository.find_trip_by_id(trip_id)
    print(trip)

def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    trips_repository = TripRepository(conn)

    trips_repository.update_trip_status(trip_id)
