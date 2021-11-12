import pyodbc

class Database:
    def __init__(self):
        self.driver = 'DRIVER={SQL Server};'
        self.server = 'SERVER=DESKTOP-TM5VSPQ\SQLEXPRESS;'
        self.db = 'DATABASE=MANAGE_IT;'
        self.tc = 'Trusted_Connection=yes;'
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