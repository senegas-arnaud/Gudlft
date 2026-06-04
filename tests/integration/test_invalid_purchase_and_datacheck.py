import server

def test_invalid_purchase_datacheck(client):
    response = client.post('/showSummary', data={'email': 'admin@irontemple.com'})
    assert b'Welcome' in response.data

    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Iron Temple',
        'places': '10'
    })
    assert response.status_code == 200
    assert b'Your club dont have enough point' in response.data
    
    # Data unchanged in json
    clubs = server.loadClubs()
    iron_temple = [c for c in clubs if c['name'] == 'Iron Temple'][0]
    assert int(iron_temple['points']) == 4