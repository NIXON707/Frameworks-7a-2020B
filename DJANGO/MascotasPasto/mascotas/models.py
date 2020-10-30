from django.db import models

# Create your models here.
class Tipos (models.Model) :
    code = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    abreviatura = models.CharField(max_length=10)
    estado = models.BooleanField(default=True)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')
class Razas (models.Model) :
    code = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    abreviatura = models.CharField(max_length=10)
    id_tipos = models.ForeignKey(Tipos, null = True, blank = True, on_delete = models.CASCADE)
    estado = models.BooleanField(default=True)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')
class Mascotas (models.Model) :
    code = models.CharField(max_length=20)
    id_tipos = models.ForeignKey(Tipos, null = True, blank = True, on_delete = models.CASCADE)
    id_raza = models.ForeignKey(Razas, null = True, blank = True, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=30)
    tiene_vacunas = models.BooleanField(default=False)
    estado = models.BooleanField(default=True)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')
