from django.urls import path
from profiles_api import views
# Para usar viewset
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
"""
    Lista de URL que concuerden con las vistas del proyecto
"""
urlpatterns=[
    path('hello-view/', views.HelloApiView.as_view()), # basicamente de aqui pasa a la peticion get de http
    path('', include(router.urls)),
]