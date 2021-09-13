"""
    Importamos las siguientes clases desde el rest framework
    la segunda clase "response" se utiliza para retornar
    una respuesta estandar desde la API cuando alguno de los
    otros componentes la invoque
"""
from rest_framework.views import APIView
from rest_framework.response import Response
# Vamos a usar post o update? si, entonces agregamos esto
from rest_framework import status  # Para el manejo de respuestas de la api
from profiles_api import serializers

"""
    Creamos la clase de la API view esta nos permite definir la
    logica para el endpoint 
    Funcionamiento:
    1. Definir una URL que es nuestro endpoint y luego lo asignamos a esta
    vista 
    2. El rest framework de djando la maneja al llamar la funcion apropiada
    en la vista para la peticion http que se desea hacer  
    
    CUALQUIER FUNCION HTTP QUE AGREGUEMOS EN LA API VIEW
    DEBE RETORNAR UNA RESPUESTA
    
"""


class HelloApiView(APIView):
    """Test API VIEW"""
    serializer_class = serializers.HelloSerializer  # Esto configura la api view para recibir la clase serializer

    # Aceptamos la peticion HTTP GET
    def get(self, request,
            format=None):  # La variable request viene desde el rest framework y contiene detalles sobre la peticion que se esta haciendo a la api
        """Returns a list of APIView features"""
        # Para el ejemplo vamos a definir una lista que describa todas las caracteristicas de una API view
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to  a traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URL'
        ]
        # La rta debe contener un diccionario o lista para poder convertir la rta en un json
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    """
        Cuando recibimos una peticion POST a la API:
        1. Toma el serializer y pasa los datos que se enviaron en la 
        peticion 
        
        *la clase "serializer_class" viene por defecto y recupera el serializer 
        de la vista en un formato estandar para su manejo
        
    """

    def post(self, request):
        """Create a hello message with our name """
        serializer = self.serializer_class(
            data=request.data)  # el data=request.data asigna los datos de forma que cuendo se hace un post

        # Vamos a validar los parametros de la entrada serializer
        if serializer.is_valid():
            name = serializer.validated_data.get(
                'name')  # De esta forma retornamos el campo que creams en el archivo serializers
            message = f'Hello {name}'  # Formato para retornar el string del nombre
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                # Devolvemos los errores generados por el serializer, basicamente nos da un diccionario de todos los errores basados en el serializador
                status=status.HTTP_400_BAD_REQUEST
                # Cambiamos la rta que esta por defecto para mostrar el estado de error
            )

    # Este metodo se suele hacer hacia una primary key especifica de una url
    # En este caso no se hace pero generalmente en el 'pk' se establece el ID del objeto que se esta actualizando
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    # Usualmente se usa para actualizar los campos que estaban en la peticion
    # ej: estaba pindiendo primer y apellido, con esto puedo actualizar solo el apellido
    # en cambio con put se reemplaza todo por la entrada que genere
    # MEANING: PUT - Remplazar un objeto con uno nuevo de entrada
    # PATCH - Solo actualiza los cambios en los campos definidos en el request/peticion
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
