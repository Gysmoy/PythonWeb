from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from manage_it_service.serializers import supplier as serializers
from manage_it_service.database.query import Query


class setSupplier(APIView):
    serializer_class = serializers.setSupplier
    def post(self, request):  
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data

                tipo = postData.get('tipo')

                per_nat = postData.get('id_per_nat')
                if per_nat == '':
                    id_per_nat = None
                else:
                    id_per_nat = per_nat

                per_jur = postData.get('id_per_jur')
                if per_jur == '':
                    id_per_jur = None
                else:
                    id_per_jur = per_jur

                usuario_creacion = postData.get('usuario_creacion')
            
               
                query = Query("PROVEEDORES_CREATE",[tipo, id_per_nat, id_per_jur, usuario_creacion], 'SET')
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta'
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

class getSuppliers(APIView):
    serializer_class = serializers.idUser
    def post(self, request):
        res={}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data']=[]
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                id_user = postData.get('id_user')
                query = Query('PROVEEDORES_READ_ALL',[id_user] )
                if query.status:
                    res['status']=200
                    res['message'] = 'Operacion Correcta'
                    res['data']=query.getAll()
                else:
                    res['message'] = query.message
            else:
                res['message'] = 'Error en la operacion'
        except Exception as e:
            res['status']=400
            res['message']= 'Error en la peticion' + e
        finally:
            if (res['status'] == '200'):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class getActivesSuppliers(APIView):
    serializer_class = serializers.idUser
    def post(self, request):
        res={}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data']=[]
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                id_user = postData.get('id_user')
                query = Query('PROVEEDORES_READ_ACTIVES',[id_user] )
                if query.status:
                    res['status']=200
                    res['message'] = 'Operacion Correcta'
                    res['data']=query.getAll()
                else:
                    res['message'] = query.message
            else:
                res['message'] = 'Error en la operacion'
        except Exception as e:
            res['status']=400
            res['message']= 'Error en la peticion' + e
        finally:
            if (res['status'] == '200'):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)
class getInactivesSuppliers(APIView):
    serializer_class = serializers.idUser
    def post(self, request):
        res={}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data']=[]
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                id_user = postData.get('id_user')
                query = Query('PROVEEDORES_READ_INACTIVES',[id_user] )
                if query.status:
                    res['status']=200
                    res['message'] = 'Operacion Correcta'
                    res['data']=query.getAll()
                else:
                    res['message'] = query.message
            else:
                res['message'] = 'Error en la operacion'
        except Exception as e:
            res['status']=400
            res['message']= 'Error en la peticion' + e
        finally:
            if (res['status'] == '200'):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class updateSupplier(APIView):
    serializer_class = serializers.updateSupplier
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
                tipo = postData.get('tipo')
                per_nat = postData.get('id_per_nat')
                per_jur = postData.get('id_per_jur')
                query = Query("PROVEEDORES_UPDATE",[id, tipo, id_per_nat, id_per_jur], 'SET')
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
            res['message'] = 'Error' +e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)
class deleteSupplier(APIView):
    serializer_class = serializers.idSupplier
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                id = serializer.validated_data.get('id')
                query = Query("PROVEEDORES_DELETE",[id], 'SET')
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
class restoreSupplier(APIView):
    serializer_class = serializers.idSupplier
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                id = serializer.validated_data.get('id')
                query = Query("PROVEEDORES_RESTORE",[id], 'SET')
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