from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from manage_it_service.serializers import subs as serializers
from manage_it_service.database.query import Query

class setSubscription(APIView):
    serializer_class = serializers.setSubscriptions
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

                id_proveedor = postData.get('id_proveedor')
                id_ciclos = postData.get('id_ciclos')
                id_moneda = postData.get('id_moneda')
                monto = postData.get('monto')
                fec_inicio = postData.get('fec_inicio')
                prorroga = postData.get('prorroga')
                usuario = postData.get('usuario_creacion')
               
                query = Query("SUBSCRIPCIONES_CREATE",[id_proveedor, id_ciclos, id_moneda, monto, fec_inicio, prorroga, usuario], 'SET')
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

class getSubscriptiones(APIView):
    serializer_class = serializers.idSub
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
                query = Query("SUBSCRIPCIONES_READ_ALL",[id])
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

class getActiveSubscription(APIView):
    serializer_class = serializers.idSub
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
                query = Query("SUBSCRIPCIONES_READ_ACTIVES",[id])
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

class getInactiveSubscription(APIView):
    serializer_class = serializers.idSub
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
                query = Query("SUBSCRIPCIONES_READ_INACTIVES",[id])
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

class updateSubscription(APIView):
    serializer_class = serializers.updateSubs
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
                id = postData.get('id')
                id_proveedor = postData.get('id_proveedor')
                id_ciclos = postData.get('id_ciclos')
                id_moneda = postData.get('id_moneda')
                monto = postData.get('monto')
                fec_inicio = postData.get('fec_inicio')
                prorroga = postData.get('prorroga')
            
                query = Query("SUBSCRIPCIONES_UPDATE",[id, id_proveedor, id_ciclos, id_moneda, monto, fec_inicio, prorroga], 'SET')
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

class deleteSubscription(APIView):
    serializer_class = serializers.idSub
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                id = serializer.validated_data.get('id')
                query = Query("SUBSCRIPCIONES_DELETE",[id], 'SET')
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta'
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

class restoreSubscription(APIView):
    serializer_class = serializers.idSub
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                id = serializer.validated_data.get('id')
                query = Query("SUBSCRIPCIONES_RESTORE",[id], 'SET')
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta' 
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