from server import app


def test_unknown_email(client):
    response = client.post('/showSummary', data={'email': 'inconnu@test.com'})
    assert response.status_code == 200
    assert b'Sorry, that email was not found' in response.data


def test_valid_email(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'Welcome' in response.data