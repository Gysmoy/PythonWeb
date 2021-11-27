
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from manage_it_service.serializers import persona as serializers
from uuid import uuid4
from hashlib import sha256
from manage_it_service.database.query import Query

# hacer que te reciba en actualizzar dato telefono nulo

# Persona Natural

class setPNatural(APIView):
    serializer_class = serializers.setP_naturalSerializer
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                apePater = postData.get('apePater')
                apeMater = postData.get('apeMater')
                nombres = postData.get('nombres')
                dni = postData.get('dni')
                id_servicio = postData.get('id_servicio')
                tel1 = postData.get('tel1')
                tel2 = postData.get('tel2')
                correo = postData.get('correo')
                direccion = postData.get('direccion')
                id_user = postData.get('id_user')
                query = Query("PERSONA_NATURAL_CREATE",[apePater, apeMater, nombres, dni, id_servicio, tel1, tel2, correo, direccion, id_user], 'SET')
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

class getPNaturales(APIView):
    serializer_class = serializers.idPer
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
                query = Query("PERSONA_NATURAL_READ_ALL",[id])
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

class getActivePNaturales(APIView):
    serializer_class = serializers.idPer
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
                query = Query("PERSONA_NATURAL_READ_ACTIVES",[id])
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

class getInactivePNaturales(APIView):
    serializer_class = serializers.idPer
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
                query = Query("PERSONA_NATURAL_READ_INACTIVES",[id])
                if query.status:
                        res['status'] = 200
                        res['message'] = 'Persona Natural Activas '
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

class updatePNatural(APIView):
    serializer_class = serializers.updateP_naturalSerializer
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
                apePater = postData.get('apePater')
                apeMater = postData.get('apeMater')
                nombres = postData.get('nombres')
                dni = postData.get('dni')
                id_servicio = postData.get('id_servicio')
                tel1 = postData.get('tel1')
                tel2 = postData.get('tel2')
                correo = postData.get('correo')
                direccion = postData.get('direccion')
                query = Query("PERSONA_NATURAL_UPDATE",[id, apePater, apeMater, nombres, dni, id_servicio, tel1, tel2, correo, direccion], 'SET')
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Persona Natural Actualizada Correctamente'
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

class deletePNatural(APIView):
    serializer_class = serializers.idPer
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                id = serializer.validated_data.get('id')
                query = Query("PERSONA_NATURAL_DELETE",[id], 'SET')
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Persona Natural Eliminada Correctamente'
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

class restorePNatural(APIView):
    serializer_class = serializers.idPer
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                id = serializer.validated_data.get('id')
                query = Query("PERSONA_NATURAL_RESTORE",[id], 'SET')
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Persona Natural Recuperada Correctamente' 
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

# Persona Juridica

class setPJuridica(APIView):
    serializer_class = serializers.setPjuridicaSerializer
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []

        try:
            
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                res['message'] = 'dentro de try, if' 
                postData = serializer.validated_data
                RSocial = postData.get('razonSocial')
                ruc = postData.get('ruc')
                id_servicio = postData.get('id_servicio')
                tel1 = postData.get('tel1')
                tel2 = postData.get('tel2')
                correo = postData.get('correo')
                direccion = postData.get('direccion')
                id_user = postData.get('id_user')
                
                query = Query("PERSONA_JURIDICA_CREATE",[RSocial, ruc, id_servicio, tel1,tel2, correo, direccion,id_user], 'SET')
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Persona Juridica Creada Correctamente'
                    res['data'] = query.getAll()
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

class getPJuridica(APIView):
    serializer_class = serializers.idPer
    def post(self, request):
        res={}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data']=[]
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                id = postData.get('id')
                query = Query('PERSONA_JURIDICA_READ_ALL',[id] )
                if query.status:
                    res['status']=200
                    res['message'] = 'Listar Datos de Persona Juridica Realizado Correctamente'
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

class getActivePJuridica(APIView):
    dserializer_class = serializers.idPer
    def post(self, request):
        res={}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data']=[]
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                id = postData.get('id')
                query = Query('PERSONA_JURIDICA_READ_ACTIVES',[id] )
                if query.status:
                    res['status']=200
                    res['message'] = 'Listar Datos Activos de Persona Juridica realizado Correctamente'
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

class getInactivePJuridica(APIView):
    serializer_class = serializers.idPer
    def post(self, request):
        res={}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data']=[]
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                id = postData.get('id')
                query = Query('PERSONA_JURIDICA_READ_INACTIVES',[id] )
                if query.status:
                    res['status']=200
                    res['message'] = 'Listar Datos Inactivos de Persona Juridica realizado Correctamente'
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
 
class updatePJuridica(APIView):
    serializer_class = serializers.updatePJuridicaSerializer
    def post(self, request):
        res={}
        res['status']=400
        res['message']='NTS'
        res['data']=[]
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                id = postData.get('id')
                RSocial = postData.get('razonSocial')
                ruc = postData.get('ruc')
                id_servicio = postData.get('id_servicio')
                tel1 = postData.get('tel1')
                tel2 = postData.get('tel2')
                correo = postData.get('correo')
                direccion = postData.get('direccion') 
                query = Query('PERSONA_JURIDICA_UPDATE', [id, RSocial, ruc, id_servicio, tel1, tel2, correo, direccion], 'SET')
                if query.status:
                    res['status']=200
                    res['message']='Operacion Correcta'
                else:
                    res['message'] = query.message
            else:
                res['status']=400
                res['message']='Error en la peticion'
        except Exception as e:
            res['status']=400
            res['message']='Error'+e
        finally:
            if (res['status']==200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class deletePJuridica(APIView):
    serializer_class = serializers.idPer
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                id = serializer.validated_data.get('id')
                query = Query("PERSONA_JURIDICA_DELETE",[id], 'SET')
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
                
class restorePJuridica(APIView):
    serializer_class = serializers.idPer
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                id = serializer.validated_data.get('id')
                query = Query("PERSONA_JURIDICA_RESTORE",[id], 'SET')
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

