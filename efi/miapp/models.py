from django.db import models

# Create your models here.

class Garcia_Persona(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    nombre = models.CharField(max_length=150, verbose_name="Título")
    apellido = models.CharField(max_length=150,verbose_name="Contenido")
    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        verbose_name="Sexo"
    )
    fecha_de_registro = models.DateTimeField(auto_now_add=True)
