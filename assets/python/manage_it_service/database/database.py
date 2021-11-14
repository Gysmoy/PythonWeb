import pyodbc
import json
from os import environ
from os.path import dirname, abspath

config_db = dirname(abspath(__file__)) + '\\config.json'

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