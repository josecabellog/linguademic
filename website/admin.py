from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edades', 'precio', 'activo', 'orden')
    list_editable = ('activo', 'orden')
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ('nombre', 'descripcion_corta')
    list_filter = ('activo',)