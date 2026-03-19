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
    descripcion_larga = models.TextField(blank=True, help_text="Descripción detallada del curso")
    imagen_hero = models.ImageField(upload_to='cursos/', blank=True, null=True, help_text="Imagen para la sección hero")
    incluye = models.TextField(blank=True, help_text="Escribe cada item en una línea nueva")

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('detalle_curso', args=[self.slug])
    
    def lista_incluye(self):
        """Convierte el texto en una lista, separando por líneas"""
        if self.incluye:
            return [item.strip() for item in self.incluye.split('\n') if item.strip()]
        return []
    
    class Meta:
        ordering = ['orden', 'nombre']
