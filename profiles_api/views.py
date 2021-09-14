"""
    Importamos las siguientes clases desde el rest framework
    la segunda clase "response" se utiliza para retornar
    una respuesta estandar desde la API cuando alguno de los
    otros componentes la invoque
"""
from rest_framework.views import APIView
from rest_framework.response import Response
# Vamos a usar put o patch? si si entonces
from rest_framework import status
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
    serializer_class = serializers.HelloSerializer
    # Aceptamos la peticion HTTP GET
    def get(self, request, format=None): # La variable request viene desde el rest framework y contiene detalles sobre la peticion que se esta haciendo a la api
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

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})