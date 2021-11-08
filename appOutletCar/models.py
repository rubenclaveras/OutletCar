from django.db import models

class Coche(models.Model):
    id= models.AutoField(primary_key= True)
    marca= models.CharField(max_length= 15)
    modelo= models.CharField(max_length= 35)
    kilometros= models.IntegerField()
    categoria= models.CharField(max_length= 300)
    color= models.CharField(max_length= 20)
    precio= models.IntegerField()