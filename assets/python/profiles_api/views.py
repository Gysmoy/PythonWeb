from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    '''API view de prueba'''
    def get(self, request, format=None):
        an_apiview = ['data','de','base de  datos']

        return Response({'status':'200','message':'Listado Terminado','data':an_apiview})

