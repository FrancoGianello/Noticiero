from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Noticia, Autor
# Create your views here.

def index(request):
    noticias = Noticia.objects.all().order_by("-id")
    template = loader.get_template("Noticias/index.html")
    context = {
        "noticias" : noticias,
    }
    return HttpResponse(template.render(context, request))

def detalle(request, detalle):
    noticia = Noticia.objects.get(titulo=detalle)
    template = loader.get_template("Noticias/detalle.html")
    context = {
        "noticia" : noticia,
    }
    return HttpResponse(template.render(context, request))

def autor(request, autor):
    autor = Autor.objects.get(nombre=autor)
    noticiasAutor = Noticia.objects.filter(autor=autor)
    template = loader.get_template("Noticias/autor.html")
    context = {
        "noticias" :noticiasAutor,
        "autor" : autor,
    }
    return HttpResponse(template.render(context, request))