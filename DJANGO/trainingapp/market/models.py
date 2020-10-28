from django.db import models

# Create your models here.
class Category (models.Model) :
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')
class Vendor (models.Model) :
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
