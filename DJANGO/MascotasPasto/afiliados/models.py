from django.db import models

# Create your models here.
class Paises (models.Model) :
    code = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    abreviatura = models.CharField(max_length=10)
    estado = models.BooleanField(default=True)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')
class Ciudades (models.Model) :
    code = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    abreviatura = models.CharField(max_length=10)
    id_paises = models.ForeignKey(Paises, null = True, blank = True, on_delete = models.CASCADE)
    estado = models.BooleanField(default=True)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')
class Afiliados (models.Model) :
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    numero_movil = models.BigIntegerField(default='')
    direccion = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    id_ciudades = models.ForeignKey(Ciudades, null = True, blank = True, on_delete = models.CASCADE)
    estado = models.BooleanField(default=True)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')
    