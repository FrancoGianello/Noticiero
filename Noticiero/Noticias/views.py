from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Noticia, Autor
# Create your views here.

def index(request):
    return render(request,"Noticias/index.html", {
        "noticias": Noticia.objects.all().order_by("-id"),
        })

def detalle(request, detalle):
    return render(request, "Noticias/detalle.html",{
        "noticia":get_object_or_404(Noticia, titulo=detalle),
    })

def autor(request, autor):    
    autor = Autor.objects.get(nombre=autor)
    # Es IMPORTANTISIMO coger el nombre, porque al hacer la query de noticias por autor hay que comparar con una consulta previa
    return render(request, "Noticias/autor.html", {
        "autor" : get_object_or_404(Autor, nombre=autor),
        "noticias" : Noticia.objects.filter(autor=autor),
    })