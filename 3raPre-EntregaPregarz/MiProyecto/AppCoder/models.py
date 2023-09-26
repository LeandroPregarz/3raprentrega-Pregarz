from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

    
class Computadora(models.Model):
    placaMadre = models.CharField(max_length=40)
    placaVideo = models.CharField(max_length=40)
    procesador = models.CharField(max_length=40)
    ram = models.CharField(max_length=40)
    fuente = models.CharField(max_length=40)
    almacenamiento = models.CharField(max_length=40)
    
class Perifericos(models.Model):
    teclado = models.CharField(max_length=40)
    mouse = models.CharField(max_length=40)
    monitor = models.CharField(max_length=40)
    headset = models.CharField(max_length=40)
    
class Plataforma(models.Model):
    nombrePlataforma = models.CharField(max_length=40)
    user = models.CharField(max_length=40)
    mail = models.EmailField()
    
    
    
    
    

    


