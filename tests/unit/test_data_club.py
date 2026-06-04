import server

def test_data_club(client):
    client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '5'
    })

    clubs_from_json = server.loadClubs()
    club = [c for c in clubs_from_json if c['name'] == 'Simply Lift'][0]
    assert int(club['points']) == 10