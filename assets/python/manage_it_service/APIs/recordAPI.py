from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from manage_it_service.serializers import record as serializers
from manage_it_service.database.query import Query

class setRecord(APIView):
    serializer_class = serializers.setRecord
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            print(serializer)
            if serializer.is_valid():  
                postData = serializer.validated_data
                id_pr = postData.get('id_pr')
                monto = postData.get('monto')
                usuario_creacion = postData.get('usuario_creacion')
                query = Query("HISTORIALES_CREATE",[id_pr,monto, usuario_creacion], 'SET')
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta'
                    res['data'] = query.getAll()
                else:
                    res['message'] = query.message + str(serializer)
            else:
                res['status'] = 400
                res['message'] = 'Error en la Peticion'+str(serializer)
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' +e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class getRecords(APIView):
    serializer_class = serializers.idRecord
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
                query = Query("HISTORIALES_READ_ALL",[id])
                if query.status:
                        res['status'] = 200
                        res['message'] = 'Operacion Correcta'
                        res['data'] = query.getAll()
                else:
                    res['message'] = query.message
            else:
                res['message'] = 'Error en la operacion'
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)
