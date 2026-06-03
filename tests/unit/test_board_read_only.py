def test_board_read_only(client):
    response = client.get('/pointsBoard')
    assert b'<form' not in response.data