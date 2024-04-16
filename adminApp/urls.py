from django.urls import path
from . import views 

urlpatterns = [
    path('', views.layout, name='layout'),
    path('agregar', views.agregar, name='agregar'),
    path('listar', views.listar, name='listar'),
    path('actualizar/<int:id>', views.actualizar, name='actualizar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    
]