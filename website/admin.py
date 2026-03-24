from django.contrib import admin
from .models import Curso, Recurso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edades', 'precio', 'activo', 'orden')
    list_editable = ('activo', 'orden')
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ('nombre', 'descripcion_corta')
    list_filter = ('activo',)

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_publicacion', 'activo')
    list_editable = ('activo',)
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo', 'descripcion_corta')
    list_filter = ('categoria', 'activo')
    date_hierarchy = 'fecha_publicacion'