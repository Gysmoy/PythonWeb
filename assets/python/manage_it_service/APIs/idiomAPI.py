from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from manage_it_service.serializers import idiom as serializers
from uuid import uuid4
from hashlib import sha256
from manage_it_service.database.query import Query


class setIdiom(APIView):
    serializer_class = serializers.setIdiomSerializer
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []

        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                idiom = postData.get('idiom')
                query = Query('IDIOMAS_CREATE',[idiom], 'SET')
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Idioma Agregado Correctamente'
                    res['data'] = query.getAll()
                else:
                    res['message'] = query.message
            else:
                res['status'] = 400
                res['message'] = 'Error en la Peticion'
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' +e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class getIdioms(APIView):
   def get(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            query = Query("IDIOMAS_READ_ALL")
            if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta'
                    res['data'] = query.getAll()
            else:
                res['message'] = query.message
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class getActiveIdioms(APIView):
     def get(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            query = Query("IDIOMAS_READ_ACTIVES")
            if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta'
                    res['data'] = query.getAll()
            else:
                res['message'] = query.message
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class getInactiveIdioms(APIView):
    def get(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            query = Query("IDIOMAS_READ_INACTIVES")
            if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta'
                    res['data'] = query.getAll()
            else:
                res['message'] = query.message
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class updateIdiom(APIView):
    serializer_class = serializers.updateIdiomSerializer
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []

        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                id = postData.get('id')
                idiom = postData.get('idiom')
                query = Query('IDIOMAS_UPDATE',[id, idiom], 'SET')
                print(serializer)
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Idioma Actualizado Correctamente'
                    res['data'] = query.getAll()
                else:
                    res['message'] = query.message
            else:
                res['status'] = 400
                res['message'] = 'Error en la Peticion'
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' +e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class deleteIdiom(APIView):
    serializer_class = serializers.datIdiomSerializer
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                dat = serializer.validated_data.get('dat')
                query = Query("IDIOMAS_DELETE",[dat], 'SET')
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Idioma Eliminada'
                else:
                    res['message'] = query.message
            else:
                res['status'] = 400
                res['message'] = 'Error en la Peticion'
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class restoreIdiom(APIView):
    serializer_class = serializers.datIdiomSerializer
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                dat = serializer.validated_data.get('dat')
                query = Query("IDIOMAS_RESTORE",[dat], 'SET')
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Idioma Recuperado'
                else:
                    res['message'] = query.message
            else:
                res['status'] = 400
                res['message'] = 'Error en la Peticion'
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

