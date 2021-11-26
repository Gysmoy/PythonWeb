from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from manage_it_service.serializers import admin as serializers
from manage_it_service.database.query import Query

class queryAdmin(APIView):
    serializer_class = serializers.queryAdmin
    res = {}
    res['status'] = 400
    res['message'] = 'NTS'
    res['data'] = []

    def getParam(self, queryy):
        query = Query(queryy, [], '')
        if query.status:
            self.res['status'] = 200
            self.res['data'] = query.getAll()
        else:
            self.res['status'] = 400
            self.res['data'] = []
        return self.res

    def postParam(self, queryy, param =[], type='SET'):
        query = Query(queryy,param,type)
        if query.status:
            self.res['status']=200
            self.res['data'] = query.getAll()
        else:
            self.res['status'] = 400
            self.res['data'] =  []
        return self.res

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                queryy = serializer.validated_data.get('query')
                if('CREATE' in queryy or 'create' in queryy):

                    if ('TABLE' in queryy or 'TABLE' in queryy):
                        data=self.postParam(queryy)
                        if (data['status']==200):
                            data['message'] = 'Creacion de Tabla Realizados Correctamente'
                        else:
                            data['message'] = 'No se ha Podido Crear la Tabla'

                    elif('DATABASE' in queryy or 'database' in queryy):
                        data=self.postParam(queryy)
                        if (data['status']==200):
                            data['message'] = 'Creacion de Base de Datos Realizados Correctamente'
                        else:
                            data['message'] = 'No se ha Podido Crear la Base de Datos'

                    elif('PROCEDURE' in queryy or 'procedure' in queryy):
                        data=self.postParam(queryy)
                        if (data['status']==200):
                            data['message'] = 'Creacion de procedimiento Realizados Correctamente'
                        else:
                            data['message'] = 'No se ha Podido Crear la El prosedimiento Almacenado'

                elif('EXEC' in queryy or 'exec' in queryy):
                    data=self.getParam(queryy)
                    if (data['status']==200):
                        data['message'] = 'Ejecusion de Procedimiento Almacenado Realizados Correctamente'
                    else:
                        data['message'] = 'No se pudo ejecutar la El prosedimiento Almacenado'

                elif('SELECT' in queryy or 'select' in queryy):
                    data=self.getParam(queryy)
                    if (data['status']==200):
                        data['message'] = 'Listado de Datos Realizados Correctamente'
                    else:
                        data['message'] = 'No se pudo ejecutar la consulta SELECT'


                elif('UPDATE' in queryy or 'update' in queryy):
                    data=self.postParam(queryy)
                    if (data['status']==200):
                        data['message'] = 'Actualizacin de Datos Realizados Correctamente'
                    else:
                        data['message'] = 'No se ha podido actualizar los datos'
                    

                elif('DELETE' in queryy or 'delete' in queryy):
                    data=self.postParam(queryy)
                    if (data['status']==200):
                        data['message'] = 'Eliminacion de Datos Realizados Correctamente'
                    else:
                        data['message'] = 'No se ha podido eliminar los datos'

                elif('INSERT' in queryy or 'insert' in queryy):
                    data=self.postParam(queryy)
                    if (data['status']==200):
                        data['message'] = 'Agregacion de Datos Realizados Correctamente'
                    else:
                        data['message'] = 'No se ha podido agregar los datos'
                else:
                    self.res['status']=400
                    self.res['message']='Sentencia SQL no Encontrada'
            else:
                self.res['status'] = 400
                self.res['message'] = 'Error en la consulta'
        except Exception as e:
            self.res['status'] = 400
            self.res['message'] = 'Error' + e
        finally:
            if (self.res['status'] == 200):
                return Response(self.res, status.HTTP_200_OK)
            else:
                return Response(self.res, status.HTTP_400_BAD_REQUEST)

            


