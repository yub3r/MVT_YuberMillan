from django.db import models

class Familiar(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    parentesco= models.CharField(max_length=20)
    edad= models.IntegerField()
    directo= models.BooleanField()

class Mascota(models.Model):
    clase= models.CharField(max_length=20)
    nombre= models.CharField(max_length=20)


