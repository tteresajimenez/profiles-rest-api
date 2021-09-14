from django.urls import path, include # Este lo agregamos para uso en las viewsets
# Vamos a importar el default router
from rest_framework.routers import DefaultRouter
from profiles_api import views

"""
    Lista de URL que concuerden con las vistas del proyecto
"""
# Para utilizar los default routers los asignamos a una variable
router = DefaultRouter()
"""
    Ahora vamos a definir viewsets especificos en una ruta
    Genera una lista de urls que estan asociadas al viewset
    de este modo determina todas las url que son requeridas 
    para todas las funciones que se definan en el viewset
"""
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns=[
    # Registro de la APIView
    path('hello-view/', views.HelloApiView.as_view()), # basicamente de aqui pasa a la peticion get de http
    # dejamos en blanco al principio porque no queremos poner un prefijo a la url, queremos incluirlas todas
    path('', include(router.urls)) # despues pasa esta lista de url usando la funcion path y la funcion include

]