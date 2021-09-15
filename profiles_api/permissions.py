"""
Este nuevo archivo nos permitira delimitar las funciones
de los usuarios, antes de tener este archivo cualquier
usuario podia modificar la informacion de los demas
"""

from rest_framework import permissions

# Esta clase devuelve un true/false segun el caso de que el usuario pueda generar cambios
class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # Confirmamos si el metodo que se esta pidiendo es un safe methods - no generan cambios en el objeto por ej: get
        if request.method in permissions.SAFE_METHODS:
            return True
        # En caso de que no sea un safe method entonces vamos a comparar el id del objeto objetivo vs el id de quien realiza la peticion
        # True si el usuario esta tratando de actualizar su propio perfil
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id


