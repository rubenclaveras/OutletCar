from django.db import models
from django.db.models.fields.reverse_related import ManyToOneRel

class Categoria(models.Model):
    id= models.AutoField(primary_key= True)
    nombre= models.CharField(max_length= 20)

    def __str__(self):
        return self.nombre

class Coche(models.Model):
    id= models.AutoField(primary_key= True)
    marca= models.CharField(max_length= 15)
    modelo= models.CharField(max_length= 35)
    kilometros= models.IntegerField()
    anyo= models.IntegerField ()
    color= models.CharField(max_length= 20)
    precio= models.IntegerField()
    categorias= models.ManyToManyField(Categoria)

    def __str__(self):
        completo = self.marca + " " + self.modelo
        return completo