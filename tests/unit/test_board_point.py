import server

def test_board_points(client):
    response = client.get('/pointsBoard')
    
    clubs_from_json = server.loadClubs()
    for club in clubs_from_json:
        assert str(club['points']).encode() in response.data