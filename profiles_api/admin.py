from django.contrib import admin
# Importamos los modelos desde el proyecto profiles API
from profiles_api import models

"""
    Aqui registramos los modelos que vamos generando para que el 
    admin de django los muestre

    Admin de Django -> Permite crear un sitio web de administracion 
    para inspeccionar la DB y sus modelos
"""
# Registramos los modulos
admin.site.register(models.UserProfile)  # le dice al admin que registre el perfil de usuario
admin.site.register(models.ProfileFeedItem)
