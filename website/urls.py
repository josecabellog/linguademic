from django.urls import path
from .views import HomePageView, detalle_curso, aprender_index, aprender_categoria, aprender_articulo

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('curso/<slug:slug>/', detalle_curso, name='detalle_curso'),
    path('aprender/', aprender_index, name='aprender_index'),
    path('aprender/categoria/<str:categoria>/', aprender_categoria, name='aprender_categoria'),
    path('aprender/<slug:slug>/', aprender_articulo, name='aprender_articulo'),
]