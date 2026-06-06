from locust import HttpUser, task, between

class GudlftUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def view_board(self):
        self.client.get('/')

    @task
    def login(self):
        self.client.post('/showSummary', data={'email': 'john@simplylift.co'})

    @task
    def book(self):
        self.client.get('/book/Spring Festival/Simply Lift')

    @task
    def purchase(self):
        self.client.post('/purchasePlaces', data={
            'competition': 'Spring Festival',
            'club': 'Simply Lift',
            'places': '2'
        })

    @task
    def points_board(self):
        self.client.get('/pointsBoard')