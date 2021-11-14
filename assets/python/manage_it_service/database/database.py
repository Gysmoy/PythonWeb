import pyodbc
import json
from os import environ
from os.path import dirname, relpath

<<<<<<< HEAD

data = 'assets/python/manage_it_service/database/config.json'
=======
config_db = dirname(relpath(__file__)) + '\\config.json'
>>>>>>> 8685d2a9382412cd559d39727f7cc7e726cd53b4

class Database:
    def __init__(self):
        with open(config_db) as file:
            config = json.load(file)
        self.driver = 'DRIVER=' + config['driver'] + ';'
        self.server = 'SERVER=' + environ['COMPUTERNAME'] + '\\' + config['server'] + ';'
        self.db = 'DATABASE=' + config['db'] + ';'
        self.tc = 'Trusted_Connection=' + ('yes' if config['tc'] else 'no') + ';' 
        self.connection = None
    def connect(self):
        try:
            self.connection = pyodbc.connect(self.driver + self.server + self.db + self.tc)
            cursor = self.connection.cursor()
        except Exception as e:
            cursor = False
        finally:
            return cursor
    def disconnect(self):
        try:
            self.connection.close()
        except Exception as e:
            print(e)