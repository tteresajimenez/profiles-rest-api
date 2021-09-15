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
from rest_framework import viewsets

from profiles_api import permissions # Importamos el archivo donde se especificaron los permisos
from rest_framework.authentication import TokenAuthentication  # Para aplicar los permisos
"""
    El tokenAuthentication sera la variable que usemos para que los
    usuarios se autentiquen a si mismos
    ¿Como? 
    - genera un token random de tipo string cuando el usuario ingresa
    - En cada peticion que necesitemos autenticar implementamos el token en el request
"""

from rest_framework import filters # Para poder buscar perfiles por un nombre especiico

from profiles_api import serializers
from profiles_api import models

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
    """Test API Viewset"""
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
"""
    Clase para crear el viewset
    Acciones que se ejecutan usualmente en un api
"""

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""
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

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # Vamos a configurar de forma que genere la autenticacion
    authentication_classes = (TokenAuthentication,) # Agregamos la coma para que se cree como tupla, se pueden agregar mas metodos de autenticacion que tambien se pondrian aqui
    # ahora vamos a definir las clases de permiso (permission clasees) estas especifican como el usuario obtiene los permisos
    permission_classes = (permissions.UpdateOwnProfile,) # Esto conficura el userprofileviewset para usar el token
    # Permitir los filtros
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)  # Le dice al filtro backend que campos queremos usar para permitir la busqueda
    """
        Esto genera un boton de filtro en el navegador 
        ¿Como funciona?
        1. El boton agrega el parametro de busqueda como un get
        esto se observa en la url
        http://127.0.0.1:8000/api/profile/?search=teresa 
        desde esta tambien podemos modificar la busqueda cambiando el ultimo parametro (teresa)
    """
