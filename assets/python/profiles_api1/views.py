from os import stat
from typing import Text
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from manage_it_service.database import Database
import json
import pyodbc
import string


class getUsers(APIView):
    '''API PARA OBTENER LOS USUARIOS'''

    def get(self, request):
        status = 200
        message = 'NTS'
        data = list()
        db = Database()
        try:
            cursor = db.connect()
            query = 'EXEC USUARIOS_READ_ALL'
            if (cursor != False):
                cursor.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    data.append([x for x in row])
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


class getUserByUsernameAndPassword(APIView):
    '''OBTENER USUARIO SEGÚN USUARIO Y CONTRASEÑA'''
    serializer_class = serializers.LoginSerializer
    def post(self, request):
        statusCode = 200
        message = 'NTS'
        data = list()
        db = Database()
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                username = serializer.validated_data.get('username')
                password = serializer.validated_data.get('password')
                cursor = db.connect()
                query = "USUARIOS_READ_USERNAME_PASSWORD ?, ?"
                parameters = (username, password)
                cursor.execute(query, parameters)
                row = cursor.fetchall()
                if (len(row) == 0):
                    statusCode = 400
                    message = 'Usuario y/o contraseña incorrectos'
                else:
                    data = (x for x in row[0])
                    statusCode = 200
                    message = 'Operación correcta'
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
                'data': data
            }
            if (statusCode == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class HelloApiView(APIView):
    '''API view de prueba'''
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        try:
            connection = pyodbc.connect(
                'DRIVER={SQL Server};SERVER=DESKTOP-TM5VSPQ\SQLEXPRESS;DATABASE=manage_it;Trusted_Connection=yes;')
            cursor = connection.cursor()
            query = "EXEC USUARIOS_SEARCH 'yopirata'"
            #params = ['yopirata']
            cursor.execute(query)
            row = cursor.fetchone()
            rows = cursor.fetchall()
            data = list()
            for row in rows:
                data.append([x for x in row])
            rows = data
            print(rows)
        except Exception as ex:
            print(ex)
            rows = []
        finally:
            connection.close()
            print('conexion finalizada')
        return Response({'status': '200', 'message': 'Listado Terminado', 'data': rows})

    def post(self, request):
        '''crear un mensaje con nuestro nombre'''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            apellido = serializer.validated_data.get('apellido')
            telefono = serializer.validated_data.get('telefono')
            gmail = serializer.validated_data.get('gmail')
            edad = serializer.validated_data.get('edad')
            data = {
                'Nombre': name,
                'Apellido': apellido,
                'Telefono': telefono,
                'Gmail': gmail,
                'Edad': edad
            }
            respuesta = (
                {'message': 'Datos recibidos correctamente', 'status': '200', 'data': data})

            with open('C:\\Users\\anonymous\\Desktop\\TFR\\PythonWeb\\assets\\python\\profiles_api\\json\\datas.json', 'w') as file:
                json.dump(respuesta, file, indent=4)
            return Response(respuesta)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        '''Maneja Actualizar un objeto'''
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        '''Menejar actualizacion parcial de un objeto'''
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        '''Brrar un Objeto'''
        return Response({'method': 'DELETE'})
