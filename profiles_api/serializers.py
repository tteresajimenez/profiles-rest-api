from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our API view"""
    name = serializers.CharField(max_length=10)
    """
        Vamos agregar un module serializer
        tiene funciones ectra para trabajar con modulos de db existentes
        en django
        Pasos:
        1. Crearlo
        2. Conectarlo con el user profile model
        
        Los model serializers se trabajan con metaclases, estas se usan para
        configurar el serializer de forma que apunte a un modelo especifico
    """


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        # A continuacion hacemos una lista de todos los campos que queremos hacer accesibles en la api / tambien se hace cuando se espera crear nuevos modelos con el serializer
        fields = ('id', 'email', 'name', 'password')
        # Haremos la contraseña write only para que no pueda traerse como peticion
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}  # Dar formato a contraseña -> ******
            }
        }

    # Vamos a sobreescribir la funcion crear debido a que dejamos la contraseña en solo write y pasa como hash
    """ 
        Siempre que creemos un objeto con el UserProfileSerializer 
        va a validar los campos entregados por el serializer y luego llamara la funcion create
        pasandole toda la data que ha sido validada 
    """
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user( # Llamamos a la funcion Create user que esta en models.py/userprofilemanager
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    # Dado el cambio en la contraseña tambien hacemos cambio en uodate
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password') #Borramos la contraseña y luego la asignamos en formato hash
            instance.set_password(password)

        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem # Relaciona el serializer con la clase profilefeeditem que esta en models.py
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
