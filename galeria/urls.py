from django.urls import path
from galeria.views import imagem, index

urlpatterns = [
    path('index.html', index, name='index'),
    path('imagem.html', imagem, name='imagem'),
]