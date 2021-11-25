
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from manage_it_service.serializers import persona as serializers
from uuid import uuid4
from hashlib import sha256
from manage_it_service.database.query import Query

# Persona Natural

class setP_natural(APIView):
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
                usuario_creacion = postData.get('usuario_creacion')
                query = Query("PERSONA_NATURAL_CREATE",[apePater, apeMater, nombres, dni, id_servicio, tel1, tel2, correo, direccion, usuario_creacion], 'SET')
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

class getP_naturales(APIView):
    serializer_class = serializers.idUser
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                id_user = postData.get('id_user')
                query = Query("PERSONA_NATURAL_READ_ALL",[id_user])
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

class getActiveP_naturales(APIView):
    serializer_class = serializers.idUser
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                id_user = postData.get('id_user')
                query = Query("PERSONA_NATURAL_READ_ACTIVES",[id_user])
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

class getInactiveP_naturales(APIView):
    serializer_class = serializers.idUser
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                id_user = postData.get('id_user')
                query = Query("PERSONA_NATURAL_READ_INACTIVES",[id_user])
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

class searchP_natural(APIView):
    serializer_class = serializers.allUseSerializer
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                dat = serializer.validated_data.get('dat')
                query = Query("PERSONA_NATURAL_SEARCH",[dat])
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
            res['message'] = 'Error' + e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class updateP_natural(APIView):
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
                estado = postData.get('estado')
                query = Query("PERSONA_NATURAL_UPDATE",[id, apePater, apeMater, nombres, dni, id_servicio, tel1, tel2, correo, direccion, estado], 'SET')
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

class deleteP_natural(APIView):
    serializer_class = serializers.allUseSerializer
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                dat = serializer.validated_data.get('dat')
                query = Query("PERSONA_NATURAL_DELETE",[dat], 'SET')
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

class restoreP_natural(APIView):
    serializer_class = serializers.allUseSerializer
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                dat = serializer.validated_data.get('dat')
                query = Query("PERSONA_NATURAL_RESTORE",[dat], 'SET')
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
                RSocial = postData.get('RSocial')
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
                    res['message'] = 'Operacion Correcta'
                    res['data'] = query.getAll()
                else:
                    res['message'] = query.message
            else:
                res['status'] = 400
                res['message'] = 'Error en la Peticion' + query.message
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            
            if ( res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class getPJuridica(APIView):
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
                query = Query('PERSONA_JURIDICA_READ_ALL',[id_user] )
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

class getActivePJuridica(APIView):
    dserializer_class = serializers.idUser
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
                query = Query('PERSONA_JURIDICA_READ_ACTIVES',[id_user] )
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

class getInactivePJuridica(APIView):
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
                query = Query('PERSONA_JURIDICA_READ_INACTIVES',[id_user] )
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

class searchPJuridica(APIView):
    serializer_class = serializers.searchAllPJuridica
    def post(self, request):
        res={}
        res['status']=400
        res['message']='NTS'
        res['data']=[]
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                dat = serializer.validated_data.get('dat')
                query = Query('PERSONA_JURIDICA_SEARCH',[dat])
                if query.status:
                    res['status'] = 200
                    res['message'] = 'Operacion Correcta'
                    res['data']=query.getAll()
                else:
                    query.message
            else:
                res['status'] = 400
                res['message'] = 'Error en la peticion'
        except Exception as e:
            res['status'] = 400
            res['message'] = 'Error' + e
        finally:
            if(res['status'] == 200):
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
                RSocial = postData.get('RSocial')
                ruc = postData.get('ruc')
                id_servicio = postData.get('id_servicio')
                tel1 = postData.get('tel1')
                tel2 = postData.get('tel2')
                correo = postData.get('correo')
                direccion = postData.get('direccion')
                estado = postData.get('estado') 
                query = Query('PERSONA_JURIDICA_UPDATE', [id, RSocial, ruc, id_servicio, tel1, tel2, correo, direccion, estado], 'SET')
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
    serializer_class = serializers.searchAllPJuridica
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                id_user = serializer.validated_data.get('dat')
                query = Query("PERSONA_JURIDICA_DELETE",[id_user], 'SET')
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
    serializer_class = serializers.searchAllPJuridica
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS' 
        res['data'] = []
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                id_user = serializer.validated_data.get('dat')
                query = Query("PERSONA_JURIDICA_RESTORE",[id_user], 'SET')
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

