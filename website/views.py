from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Curso

class HomePageView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):  # 👈 Este método está DENTRO de la clase
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.filter(activo=True).order_by('orden')
        return context

def detalle_curso(request, slug):
    curso = get_object_or_404(Curso, slug=slug, activo=True)
    return render(request, 'detalle_curso.html', {'curso': curso})