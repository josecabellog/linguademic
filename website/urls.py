from django.urls import path
from .views import HomePageView, detalle_curso

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('curso/<slug:slug>/', detalle_curso, name='detalle_curso'),

]