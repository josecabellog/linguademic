from django.db import models
from django.urls import reverse

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    edades = models.CharField(max_length=100)
    descripcion_corta = models.TextField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, blank=True)
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('detalle_curso', args=[self.slug])
    
    class Meta:
        ordering = ['orden', 'nombre']
