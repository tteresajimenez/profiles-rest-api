from django.urls import path
# Para usar viewset
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
# registramos la viewset
router.register('profile', views.UserProfileViewSet) # Como en la clase tenemos un queryset no es necesario estabecer un base_name
router.register('feed', views.UserProfileFeedViewSet)
"""
    Lista de URL que concuerden con las vistas del proyecto
"""
urlpatterns=[
    path('hello-view/', views.HelloApiView.as_view()), # basicamente de aqui pasa a la peticion get de http
    path('login/', views.UserLoginApiView.as_view()), # Agregamos la ruta para el login
    path('', include(router.urls))
]