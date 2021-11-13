from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from manage_it_service import serializers
from manage_it_service.database import Database
from uuid import uuid4
from hashlib import sha256

class setUser(APIView):
    pass

class getActiveUsers(APIView):
    pass

class getInactiveUsers(APIView):
    pass

class getUser(APIView):
    pass

class searchUsers(APIView):
    pass

class updateUser(APIView):
    pass

class deleteUser(APIView):
    pass

class getUsers(APIView):
    '''API PARA OBTENER LOS USUARIOS'''

    def get(self, request):
        status = 200
        message = 'NTS'
        data = list()
        db = Database()
        try:
            cursor = db.connect()
            query = 'USUARIOS_READ_ALL'
            if (cursor != False):
                cursor.execute(query, [])
                columns = [i[0] for i in cursor.description]
                rows = cursor.fetchall()
                for row in rows:
                    i = 0
                    one = {}
                    for x in row:
                        one[columns[i]] = x
                        i = i + 1
                    data.append(one)
                status = 200
                message = 'Operación correcta'
            else:
                status = 400
                message = 'No se pudo conectar a la BD'
        except Exception as e:
            status = 400
            message = 'Error: ' + e
        finally:
            db.disconnect()
            return Response({'status': status, 'message': message, 'data': data})


class getUserById(APIView):
    '''API PARA OBTENER USUARIO X USERNAME'''

    def post(self, request):
        pass


class validateUser(APIView):
    '''OBTENER USUARIO SEGÚN USUARIO Y CONTRASEÑA'''
    serializer_class = serializers.LoginSerializer
    def post(self, request):
        statusCode = 200
        message = 'NTS'
        data = dict()
        session = dict()
        db = Database()
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                username = postData.get('username')
                password = postData.get('password')
                password = sha256(password.encode()).hexdigest()
                cursor = db.connect()
                query = "USUARIOS_READ_USERNAME_PASSWORD ?, ?"
                parameters = (username, password)
                cursor.execute(query, parameters)
                columns = [i[0] for i in cursor.description]
                row = cursor.fetchall()
                if (len(row) == 0):
                    statusCode = 400
                    message = 'Usuario y/o contraseña incorrectos'
                else:
                    i = 0
                    for x in row[0]:
                        data[columns[i]] = x
                        i = i + 1 
                    if data['estado'] == False:
                        statusCode = 400
                        message = 'Este usuario esta inactivo'
                    else: 
                        statusCode = 200
                        message = 'Operación correcta'
                        session['uuid'] = uuid4()
                        session['rol'] = 'USER'
            else:
                statusCode = 400
                message = 'Error en la petición'
        except Exception as e:
            statusCode = 400
            message = 'Error: ' + e
        finally:
            db.disconnect()
            res = {
                'status': statusCode,
                'message': message,
                'data': data,
                'session': session
            }
            if (statusCode == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)