import sys
import os
import pytest
import server

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    with server.app.test_client() as client:
        server.clubs = server.loadClubs()
        server.competitions = server.loadCompetitions()
        yield client