import pyodbc
import json
from os.path import dirname, relpath

config_db = dirname(relpath(__file__)) + '\\config.json'

class Database:
    def __init__(self):
        with open(config_db) as file:
            config = json.load(file)
        self.driver = 'DRIVER=' + config['driver'] + ';'
        self.server = 'SERVER=' + config['server'] + ';'
        self.database = 'DATABASE=' + config['database'] + ';'
        self.username = 'UID=' + config['username'] + ';'
        self.password = 'PWD=' + config['password'] + ';'
        self.encrypt = 'ENCRYPT=' + ('yes' if config['encrypt'] else 'no') + ';'
        self.tsc = 'TrustServerCertificate=' + ('yes' if config['tsc'] else 'no') + ';'
        self.timeout = 'CONNECTION TIMEOUT=' + str(config['timeout']) + ';'
        self.connection = None
    def connect(self):
        try:
            self.connection = pyodbc.connect(f'{self.driver}{self.server}{self.database}{self.username}{self.password}{self.encrypt}{self.tsc}{self.timeout}')
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