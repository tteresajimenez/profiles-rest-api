from django.db import models

"""
Estas son las clases estandar para reescribir o modificar
el modulo de usuario que presenta django por defecto
"""
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager  # User manager que provee django por defecto

"""
    El manager se genera para que django sepa como manejar
    el modulo que creamos esto lo debemos hacer porque modificamos
    el modulo original donde django permite el manejo de usuarios 
    ya que por defecto este pide nombre/contraseña y nosotros lo
    cambiamos a email/contraseña por esto debemos generar un 
    "custom manager" que pueda manejar los usuarios con email
    en vez de nombre    
    
    En el manager se especifican funciones que permiten manipular objetos
    del modelo correspondiente al manager
"""


class UserProfileManager(BaseUserManager):
    """2. Manager for user profiles"""

    def create_user(self, email, name, password=None): #Django exige contraseña so si no se ingresa no se puede generar basicamente solo hasta que pongamos contraseña no podremos autenticar con el usuario
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email) # Normalizar el email
        user = self.model(email=email, name=name)  # Ahora vamos a crear el modulo del usuario
        #  No podemos pasar la contraseña entre parentesis por seguridad entonces
        #  para usarla encriptada utilizamos la siguiente funcion de django
        user.set_password(password)
        user.save(using=self._db) #  Guardar el modulo usuario, usualmente se especifica la db pero es buena practica ponerlo asi para soportar multibles db

        #  Retornar el usuario una vez ya se ha creado
        return user

    def create_superuser(self, email, name, password): #  No permitimos el non aqui porque todos los super usuarios deben tener contraseña
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password) #  Self no se pasa como parametro porque viene automaticamente con la funcion dado que esta en una clase

        user.is_superuser = True #  Is super_user viene de PermissionsMixin (importado al principio)
        user.is_staff = True #  Is staff lo definimos en la clase user profile
        user.save(using=self._db)

        return user
"""
Creamos una clase basada en las clases que importamos
Por lo tanto importamos todas sus funcionalidades y las podemos modificar
"""


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """1.Database model for users in the system"""
    email = models.EmailField(max_length=255,
                              unique=True)  # En este campo definimos que queremos una columna "emails" para nuestra DB ademas especiicamos que este debe ser de caracter unico
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)  # Revisar si el usuario es activo, por defecto decimos que si
    is_staff = models.BooleanField(default=False)  # El usuario es miembro del staff?

    # Manager - ver arriba
    objects = UserProfileManager()

    # En este caso estamos reasignando los valores que vienen por defecto en el modulo de usuario de django
    # para que se ajusten con lo que nosotros queremos
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    """
    Ahora vamos a definir algunas variables que django utilzara
    para interactual con el modelo de usuario que estamos generando 
    """

    def get_full_name(self):
        """Devuele el nombre del usuario"""
        return self.name

    def get_short_name(self):
        """Devuelve nombre corto(?) del usuario"""
        return self.name

    def __str__(self):
        """Devuelve el string correspondiente al email del usuario"""
        return self.email
