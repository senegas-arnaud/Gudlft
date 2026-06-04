def test_valid_input(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '5'
    })
    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data