import os
from os import path

"""
  Logic on all properties of the application; set them here explicite for dev, 
  but have them set as secrets before deployment in the cloud. 
"""

PATH = f'/run/secrets'

# todo: adjust for your development environment; must contain proper docker secrets
if path.exists('local'):
    print('using local db-connection parameters')
    PATH = 'local/nfj'


def read_secret(name: str) -> str:
    path_ = f'{PATH}/{name}'
    if os.path.isfile(path_):
        return open(path_, 'r').read().strip()
    else:
        raise EnvironmentError(f'property {name} not defined')


DB_HOST = read_secret('db_host')
DB_PORT = read_secret('db_port')
DB_DB = read_secret('db_db')
DB_USER = read_secret('db_user')
DB_PASS = read_secret('db_pass')
APP_PORT = read_secret('app_port')
