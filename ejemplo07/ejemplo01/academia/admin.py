from academia.models import Estudiante
from django.contrib import admin

# Register your models here.

class EstudianteAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('nombre', 'apellido', 'cedula', 'edad',
        'comprobar_provincia', 'calcular_anio_nacimiento')
    search_fields = ('nombre', 'cedula', 'apellido')


admin.site.register(Estudiante, EstudianteAdmin)