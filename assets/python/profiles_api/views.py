from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    '''API view de prueba'''

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        an_apiview = ['data','de','base de  datos']

        return Response({'status':'200','message':'Listado Terminado','data':an_apiview})

    def post(self, request):
        '''crear un mensaje con nuestro nombre'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message =  f'Hello {name}'
            return Response({'message':message})
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