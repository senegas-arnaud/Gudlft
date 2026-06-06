def test_places_limitation(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '14'
    })
    assert response.status_code == 200
    assert b'You can book a maximum of 12 places' in response.data