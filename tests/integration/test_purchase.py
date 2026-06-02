from server import app


def test_valid_input(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '5'
    })
    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data


def test_input_negatif(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '-10'
    })
    assert response.status_code == 200
    assert b'Invalid number input' in response.data


def test_input_none(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '0'
    })
    assert response.status_code == 200
    assert b'Invalid number input' in response.data


def test_club_point(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Iron Temple',
        'places': '6'
    })
    assert response.status_code == 200
    assert b'Your club dont have enough point' in response.data


def test_places_limitation(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '14'
    })
    assert response.status_code == 200
    assert b'You can book a maximum of 12 places' in response.data


def test_competition_places(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Fall Classic',
        'club': 'Simply Lift',
        'places': '10'
    })
    assert response.status_code == 200
    assert b'Not enough places in this competition' in response.data