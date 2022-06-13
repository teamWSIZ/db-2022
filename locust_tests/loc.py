import time
from dataclasses import asdict, dataclass
from random import randint, choice

from faker import Faker
from locust import HttpUser, task, between, FastHttpUser




class QuickstartUser(FastHttpUser):
    wait_time = between(0.001, 0.002)

    @task(1)
    def hello_world(self):
        self.client.get('/status')

    @task(5)
    def create_user(self):
        f = Faker()
        username = f.name().split()[1]
        # uruchomienie requestu typu GET, z parametrem; by w statystykach wszystko bylo zagregowane, ustawiamy
        # dodatkowy argument `name` (niestety o tej samej nazwie co parametr, ale /shrug)
        self.client.get(f'/adduser?name={username}', name='/adduser')

    #
    # @task(1)
    # def put_khresults(self):
    #     r = HKRunner(randint(0, 10000), choice(['Kenya', 'Ethiopia', 'Japan']), 2 * 3600 + randint(500, 2000))
    #     self.client.put('/results', json=asdict(r))

    def on_start(self):
        print('starting')
