from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('top5', views.top5, name='top5'),
    path('biografia/<str:slug>', views.biografia, name='biografia'),
    path('genero/<str:slug>', views.genero, name='genero'),
    path('perfil', views.perfil, name='perfil'),
    path('aluguel/<int:pk>', views.aluguel, name='aluguel'),
    path('biografias', views.biografias, name='biografias'),
    path('generos', views.generos, name='generos'),
    path('filme/<str:slug>', views.filme, name='filme')
]