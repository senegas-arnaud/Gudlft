def test_club_point(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Iron Temple',
        'places': '6'
    })
    assert response.status_code == 200
    assert b'Your club dont have enough point' in response.data