from .links_to_repository import LinksToRepository
from src.models.settings.db_connection_handler import db_connection_handler

import pytest
import uuid

db_connection_handler.connect()
link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    links_to_repository = LinksToRepository(conn)

    link_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "https://www.google.com",
        "title": "Google"
    }

    links_to_repository.registry_link(link_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_to_repository = LinksToRepository(conn)

    links = links_to_repository.find_links_from_trip(trip_id)
    
    assert isinstance(links, list)
    assert isinstance(links[0], tuple)