from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from manage_it_service.serializers import users as serializers
from manage_it_service.database.database import Database
from manage_it_service.database.query import Query
from uuid import uuid4
from hashlib import sha256

class setUser(APIView):
    serializer_class = serializers.setUser

    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []

        try:
            serializer = self.serializer_class(data=request.data)
            print(serializer)
            if serializer.is_valid():
                postData = serializer.validated_data
                usuario = postData.get('usuario')
                correo = postData.get('correo')
                clave = postData.get('clave')
                clave = sha256(clave.encode()).hexdigest()
                dni = postData.get('dni')
                apePater = postData.get('apePater')
                apeMater = postData.get('apeMater')
                nombres = postData.get('nombres')
                sexo = postData.get('sexo')
                fec_nac = postData.get('fec_nac')
                id_idioma = postData.get('id_idioma')
                query = Query("USUARIOS_CREATE", [
                              usuario, correo, clave, dni, apePater, apeMater, nombres, sexo, fec_nac, id_idioma], 'SET')
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

            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class getUsers(APIView):
    def get(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []
        try:
            query = Query("USUARIOS_READ_ALL")
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

            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class getActiveUsers(APIView):
    def get(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []
        try:
            query = Query("USUARIOS_READ_ACTIVES")
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

            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class getInactiveUsers(APIView):
    def get(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []
        try:
            query = Query("USUARIOS_READ_INACTIVES")
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

            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class updateUser(APIView):
    serializer_class = serializers.updateUserSerializer

    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []

        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                id = postData.get('id')
                usuario = postData.get('usuario')
                correo = postData.get('correo')
                clave = postData.get('clave')
                clave = sha256(clave.encode()).hexdigest()
                dni = postData.get('dni')
                apePater = postData.get('apePater')
                apeMater = postData.get('apeMater')
                nombres = postData.get('nombres')
                sexo = postData.get('sexo')
                fec_nac = postData.get('fec_nac')
                id_idioma = postData.get('id_idioma')
                query = Query("USUARIOS_UPDATE", [
                              id, usuario, correo, clave, dni, apePater, apeMater, nombres, sexo, fec_nac, id_idioma], 'SET')
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

            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

    pass

class deleteUser(APIView):
    serializer_class = serializers.idUser
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                id = serializer.validated_data.get('id')
                query = Query("USUARIOS_DELETE", [id], 'SET')
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

            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class restoreUser(APIView):
    serializer_class = serializers.idUser
    def post(self, request):
        res = {}
        res['status'] = 400
        res['message'] = 'NTS'
        res['data'] = []
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                id = serializer.validated_data.get('id')
                query = Query("USUARIOS_RESTORE", [id], 'SET')
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

            if (res['status'] == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)

class validateUser(APIView):
    serializer_class = serializers.LoginSerializer
    def post(self, request):
        statusCode = 200
        message = 'NTS'
        data = dict()
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                postData = serializer.validated_data
                username = postData.get('username')
                password = postData.get('password')
                password = sha256(password.encode()).hexdigest()
                query = Query('USUARIOS_VALIDATE', [username, password])
                if (query.status):
                    data = query.getOne()
                    if (data['estado'] == 1):
                        statusCode = 200
                        message = 'Operación correcta'
                        data = query.getOne()
                    else:
                        statusCode = 400
                        message = 'Usuario inactivo'
                        data = dict()
                else:
                    statusCode = 400
                    message = 'Usuario y/o contraseña incorrectos'
            else:
                statusCode = 400
                message = 'Error en la petición'
        except Exception as e:
            statusCode = 400
            message = 'Error: ' + e
        finally:
            res = {
                'status': statusCode,
                'message': message,
                'data': data
            }
            if (statusCode == 200):
                return Response(res, status.HTTP_200_OK)
            else:
                return Response(res, status.HTTP_400_BAD_REQUEST)
