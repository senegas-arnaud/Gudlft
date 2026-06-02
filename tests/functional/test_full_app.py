import server


def test_full_app(client):
    
    response = client.get('/')
    assert response.status_code == 200

    response = client.get('/login')
    assert response.status_code == 200

    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'Welcome' in response.data

    response = client.get('/book/Spring Festival/Simply Lift')
    assert response.status_code == 200

    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '3'
    })
    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data

    response = client.get('/logout')
    assert response.status_code == 302  