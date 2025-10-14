from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),
]