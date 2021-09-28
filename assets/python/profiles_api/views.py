from typing import Text
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
import json
import pyodbc
import string
class HelloApiView(APIView):
    '''API view de prueba'''
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        try:
            connection=pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-R089M73\SQLEXPRESS;DATABASE=manage;Trusted_Connection=yes;')
            print('concion sitosa')
            cursor = connection.cursor()
            cursor.execute('select * from usuarios;')
            row = cursor.fetchone()
            rows = cursor.fetchall()
            rows = json.dumps(rows)
            print( rows)
            with open('C:\\Users\\anonymous\\Desktop\\TFR\\PythonWeb\\assets\\python\\profiles_api\\json\\datas.json', 'w') as file:
                json.dump(rows, file, indent=4)
        except Exception as ex:
            print(ex)
        finally:
            connection.close()
            print('conexion finalizada')
        data = ['data','de','base de  datos']
        return Response({'status':'200','message':'Listado Terminado','data':data})

    def post(self, request):
        '''crear un mensaje con nuestro nombre'''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            apellido = serializer.validated_data.get('apellido')
            telefono = serializer.validated_data.get('telefono')
            gmail = serializer.validated_data.get('gmail')
            edad = serializer.validated_data.get('edad')
            data =  {
                'Nombre':name,
                'Apellido':apellido,
                'Telefono':telefono,
                'Gmail':gmail,
                'Edad':edad
            }
            respuesta=({'message':'Datos recibidos correctamente','status':'200','data':data})

            with open('C:\\Users\\anonymous\\Desktop\\TFR\\PythonWeb\\assets\\python\\profiles_api\\json\\datas.json', 'w') as file:
                json.dump(respuesta, file, indent=4)
            return Response(respuesta)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request , pk=None):
        '''Maneja Actualizar un objeto'''
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        '''Menejar actualizacion parcial de un objeto'''
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        '''Brrar un Objeto'''
        return Response({'method':'DELETE'})