import pyodbc
import json
from os import environ


data = 'assets/python/manage_it_service/database/config.json'

class Database:
    def __init__(self):
        with open(data) as file:
            connf = json.load(file)
        self.driver = connf['driver']
        self.server = 'SERVER=' + environ['COMPUTERNAME'] + '\\'+connf['server']
        self.db = connf['db']
        self.tc =connf['tc']
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