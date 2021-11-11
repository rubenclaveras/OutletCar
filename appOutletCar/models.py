from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.reverse_related import ManyToOneRel

class Marca(models.Model):
    id= models.AutoField(primary_key= True)
    nombreMarca= models.CharField(max_length= 20)
    logo= models.ImageField(upload_to="static/fotos/logosMarcas", null=True)

    def __str__(self):
        return self.nombreMarca

class Categoria(models.Model):
    id= models.AutoField(primary_key= True)
    nombreCategoria= models.CharField(max_length= 20)

    def __str__(self):
        return self.nombreCategoria

class Coche(models.Model):
    id= models.AutoField(primary_key= True)
    marca= models.ForeignKey(Marca, on_delete= models.CASCADE)
    modelo= models.CharField(max_length= 35)
    kilometros= models.IntegerField()
    anyo= models.IntegerField ()
    color= models.CharField(max_length= 20)
    precio= models.IntegerField()
    categorias= models.ManyToManyField(Categoria, through='CategoriaCoche')
    foto= models.ImageField(upload_to="static/fotos/fotosCoches", null=True)

    def __str__(self):
        completo = self.marca.nombreMarca + " " + self.modelo
        return completo

class CategoriaCoche(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    coche = models.ForeignKey(Coche, on_delete= models.CASCADE)

    def __str__(self):
        completo = self.categoria.nombreCategoria + " " + self.coche.marca.nombreMarca + " " + self.coche.modelo
        return completo