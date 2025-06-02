from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('top5', views.top5, name='top5'),
    path('biografia/<str:nome>', views.biografia, name='biografia'),
    path('genero/<str:nome>', views.genero, name='genero'),
    path('alugar/<int:pk>', views.alugar, name='alugar'),
    path('perfil', views.perfil, name='perfil'),
    path('devolver/<int:pk>', views.devolver, name='devolver')
]