from django.db import models

# Create your models here.
class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=45,null=False)
    apellido=models.CharField(max_length=80,default='S/A')
    direccion=models.TextField()

    def __str__(self) -> str:
        return self.nombre+" "+self.apellido
    