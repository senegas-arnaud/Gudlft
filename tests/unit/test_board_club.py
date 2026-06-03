import server

def test_board_clubs(client):
    response = client.get('/pointsBoard')
    clubs_from_json = server.loadClubs()
    for club in clubs_from_json:
        assert club['name'].encode() in response.data