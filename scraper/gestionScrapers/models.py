from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone

# Create your models here.
'''
class Venex(models.Model): 
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()

class FullHard(models.Model): 
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()

class Meli(models.Model): 
    id = models.AutoField(primary_key = True)
    name = models.CharField("Nombre",max_length=100, null=False)
    price = models.IntegerField("Precio", null=False)

class CompGamer(models.Model): 
    id = models.AutoField(primary_key = True)
    name = models.CharField("Nombre",max_length=100, null=False)
    price = models.IntegerField("Precio", null=False)
'''
class Product(models.Model): 
    day = timezone.now()
    formatedDay  = day.strftime("%d/%m/%Y")

    id = models.AutoField(primary_key = True)
    page = models.CharField("Página", null=False, max_length=50)
    title = models.CharField("Producto-Titulo",max_length=100, null=False)
    price = models.IntegerField("Precio", null=False)
    brand = models.CharField("Marca", null=True, blank=True, max_length=50)
    link = models.CharField("Link",max_length=500,null=True, blank=True)
    #dateFormat = models.DateTimeField(max_length=50, default=formatedDay)