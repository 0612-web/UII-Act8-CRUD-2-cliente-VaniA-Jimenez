# Create your models here.
from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.TextField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to='clientes/', blank=True, null=True, verbose_name='Foto del Cliente')

    def __str__(self):
        return f'Cliente: {self.nombre} {self.telefono}'