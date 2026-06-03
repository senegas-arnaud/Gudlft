def test_input_none(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '0'
    })
    assert response.status_code == 200
    assert b'Invalid number input' in response.data