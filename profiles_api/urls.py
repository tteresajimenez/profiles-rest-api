from django.urls import path
from profiles_api import views

"""
    Lista de URL que concuerden con las vistas del proyecto
"""
urlpatterns=[
    path('hello-view/', views.HelloApiView.as_view()), # basicamente de aqui pasa a la peticion get de http
]