import server

def test_board_no_login_required():
    with server.app.test_client() as fresh_client:
        response = fresh_client.get('/pointsBoard')
        assert response.status_code == 200