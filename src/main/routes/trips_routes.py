from flask import jsonify, Blueprint, request

trips_routes_bp = Blueprint('trips_routes', __name__)

from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder

from src.models.repositories.trips_repository import TripRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository

from src.models.settings.db_connection_handler import db_connection_handler


@trips_routes_bp.route('/trips', methods=['POST'])
def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripRepository(conn)
    emails_to_invite_repository = EmailsToInviteRepository(conn)
    controller = TripCreator(trips_repository, emails_to_invite_repository)

    response = controller.create(request.json)

    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<tripId>', methods=['GET'])
def get_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripRepository(conn)
    controller = TripFinder(trips_repository)

    response = controller.find_trip_details(tripId)

    return jsonify(response['body']), response['status_code']