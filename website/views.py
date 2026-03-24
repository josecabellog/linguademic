from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.http import Http404
from .models import Curso, Recurso, Recurso

class HomePageView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):  # 👈 Este método está DENTRO de la clase
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.filter(activo=True).order_by('orden')
        return context

def detalle_curso(request, slug):
    curso = get_object_or_404(Curso, slug=slug, activo=True)
    return render(request, 'detalle_curso.html', {'curso': curso})

def aprender_index(request):
    recursos_recientes = Recurso.objects.filter(activo=True)[:6]
    categorias = Recurso.CATEGORIAS
    
    return render(request, 'aprender/index.html', {
        'recursos_recientes': recursos_recientes,
        'categorias': categorias
    })

def aprender_categoria(request, categoria):
    recursos = Recurso.objects.filter(categoria=categoria, activo=True)
    paginator = Paginator(recursos, 9)
    page = request.GET.get('page')
    recursos_paginados = paginator.get_page(page)
    
    # Obtener el nombre de la categoría
    categorias_dict = dict(Recurso.CATEGORIAS)
    
    return render(request, 'aprender/categoria.html', {
        'recursos': recursos_paginados,
        'categoria': categorias_dict.get(categoria, categoria)
    })

def aprender_articulo(request, slug):
    recurso = get_object_or_404(Recurso, slug=slug, activo=True)
    relacionados = Recurso.objects.filter(
        categoria=recurso.categoria, 
        activo=True
    ).exclude(id=recurso.id)[:3]
    
    return render(request, 'aprender/articulo.html', {
        'recurso': recurso,
        'relacionados': relacionados
    })