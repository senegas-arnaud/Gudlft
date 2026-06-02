import server

def test_board_accessible(client):
    response = client.get('/pointsBoard')
    assert response.status_code == 200


def test_board_clubs(client):
    response = client.get('/pointsBoard')
    clubs_from_json = server.loadClubs()
    for club in clubs_from_json:
        assert club['name'].encode() in response.data


def test_board_points(client):
    response = client.get('/pointsBoard')
    
    clubs_from_json = server.loadClubs()
    for club in clubs_from_json:
        assert str(club['points']).encode() in response.data


def test_board_read_only(client):
    response = client.get('/pointsBoard')
    assert b'<form' not in response.data

def test_board_no_login_required():
    with server.app.test_client() as fresh_client:
        response = fresh_client.get('/pointsBoard')
        assert response.status_code == 200