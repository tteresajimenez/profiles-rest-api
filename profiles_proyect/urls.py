"""profiles_proyect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # Este comando lo agregamos para poder incluir las url de otras apps en el
# proyecto raiz

"""
    El proyecto busca primero por estas url y luego pasa a las derivadas
    es decir a las url que este definidas en el api
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles_api.urls')) # Generamos aqui la asignacion para la url de la api
]
