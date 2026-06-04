import server

def test_data_competition(client):
    client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '5'
    })
    
    competitions_from_json = server.loadCompetitions()
    competition = [c for c in competitions_from_json if c['name'] == 'Spring Festival'][0]
    assert int(competition['numberOfPlaces']) == 20