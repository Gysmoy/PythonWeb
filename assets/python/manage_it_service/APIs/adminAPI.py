from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from manage_it_service.serializers import admin as serializers
from uuid import uuid4
from hashlib import sha256
from manage_it_service.database.query import Query

class queryAdmin(APIView):
    serializer_class = serializers.queryAdmin

    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 200
        res['data'] = []
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                queryy = serializer.validated_data.get('query')
                if('select' in queryy or 'SELECT' in queryy):
                    m ='Usted desea listar datos'
                    query = Query(queryy)
                    if query.status:
                        res['status'] = 200
                        res['message'] = 'Operacion Correcta: ' + m
                        res['data'] = query.getAll()
                    else:
                        res['message'] = query.message + 'list'
                else:
                    update='Registro Actualizado Correctamente'
                    delete='Registro Eliminado Correctamente'
                    insert='Registro Insertado Correctamente'
                    if('UPDATE' in queryy or 'update' in queryy):
                        res['message']=update
                    elif('DELETE' in queryy or 'delete' in queryy):
                        res['message']=delete
                    else:
                        res['message']=insert
        
                    query = Query(queryy,[],'SET')
                    if query.status:
                        res['status'] = 200
                    else:
                        res['message'] = query.message + 'update,etc'
            else:
                res['status'] = 400
                res['message'] = 'Error en la consulta'
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

            


