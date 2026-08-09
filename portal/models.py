from django.db import models

# Create your models here.
class Software(models.Model):
    nivel = models.IntegerField(default=2)
    nombre = models.CharField(max_length=15, verbose_name = 'Nombre del Software')
    define = models.TextField(verbose_name = 'Descripción')

    def __str__(self):
        return "Nivel " + str(self.nivel) + " : " + self.nombre + " -> " + self.define

    class Meta:
        verbose_name = 'Herramienta de Software'
        verbose_name_plural = 'Herramientas de Software'