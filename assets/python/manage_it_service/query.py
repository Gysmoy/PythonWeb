from database import Database

class Query(Database):
    status = False
    quantity = 0
    message = 'NTS'
    def __init__(self, spu, params = []):
        self.row = dict()
        self.rows = list()
        try:
            cursor = self.connect()
            for i in range(len(params)):
                spu += ' ?,' if (i < len(params) - 1) else ' ?'
            # Ejecutando QUERY
            if (cursor != False):
                cursor.execute(spu, params)
                columns = [i[0] for i in cursor.description]
                self.rows = cursor.fetchall()
                self.quantity = len(self.rows)
            else:
                self.message = 'No se pudo conectar a la BD'
            
        except Exception as e:
            self.message = e

data = Query('USUARIOS_READ_ALL', [])
print(data.message)
print(data.quantity)
