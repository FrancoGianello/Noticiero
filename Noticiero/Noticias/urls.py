from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detalle/<str:detalle>", views.detalle, name="detalle"),
    path("autor/<str:autor>", views.autor, name="autor")
]