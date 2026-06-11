from django.db import models
import datetime
# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()

    def calcular_anio_nacimiento(self):
        return datetime.date.today().year - self.edad
    
    def comprobar_provincia(self):
        if (self.cedula.startswith("11")):
            return "Loja"
        else:
            return "Provincia no encontrada"

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, CI-Provincia: {self.comprobar_provincia()}, Edad: {self.edad}, Año de Nacimiento: {self.calcular_anio_nacimiento()}"