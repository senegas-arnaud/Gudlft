def test_competition_places(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Fall Classic',
        'club': 'Simply Lift',
        'places': '10'
    })
    assert response.status_code == 200
    assert b'Not enough places in this competition' in response.data