from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField 

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


class Recurso(models.Model):
    CATEGORIAS = [
        ('vocabulario', 'Vocabulario'),
        ('gramatica', 'Gramática'),
        ('pronunciacion', 'Pronunciación'),
        ('consejos', 'Consejos'),
        ('cultura', 'Cultura'),
    ]
    
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    descripcion_corta = models.CharField(max_length=200)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='recursos/', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('aprender_articulo', args=[self.slug])
    
    class Meta:
        ordering = ['-fecha_publicacion']