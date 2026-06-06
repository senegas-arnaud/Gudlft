
def test_login_and_purchase(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert b'Welcome' in response.data

    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '3'
    })
    assert b'Great-booking complete!' in response.data
    assert b'12' in response.data
