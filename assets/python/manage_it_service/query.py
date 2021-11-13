from database import Database

class Query():
    status = False
    quantity = 0
    message = 'NTS'
    def __init__(self, spu, params = []):
        self.row = dict()
        self.rows = list()
        db = Database()
        try:
            cursor = db.connect()
            for i in range(len(params)):
                spu += ' ?,' if (i < len(params) - 1) else ' ?'
            # Ejecutando QUERY
            if (cursor != False):
                cursor.execute(spu, params)
                columns = [i[0] for i in cursor.description]
                rows = cursor.fetchall()
                self.quantity = len(rows)
                if (self.quantity == 0):
                    self.message = 'No hay datos para mostrar'
                else:
                    for row in rows:
                        i = 0
                        one = {}
                        for x in row:
                            one[columns[i]] = x
                            i += 1
                        self.rows.append(one)
                    self.row = self.rows[0]
                    self.message = 'Operación correcta'
            else:
                self.message = 'No se pudo conectar a la BD'
        except Exception as e:
            self.message = e
    def getOne(self):
        return self.row
    def getAll(self):
        return self.rows

'''data = Query('USUARIOS_READ_ALL', [])
print(data.message)
print(data.quantity)
print(data.getOne())
print(data.getAll())'''
