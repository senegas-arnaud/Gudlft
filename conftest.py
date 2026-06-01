import sys
import os
import json
import pytest
import server

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture
def client():
    with open('clubs.json') as c:
        original_clubs = json.load(c)
    with open('competitions.json') as comps:
        original_competitions = json.load(comps)

    server.app.config['TESTING'] = True
    with server.app.test_client() as client:
        server.clubs = server.loadClubs()
        server.competitions = server.loadCompetitions()
        yield client

    with open('clubs.json', 'w') as c:
        json.dump(original_clubs, c, indent=4)
    with open('competitions.json', 'w') as comps:
        json.dump(original_competitions, comps, indent=4)