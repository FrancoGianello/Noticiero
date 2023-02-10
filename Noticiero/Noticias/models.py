from django.db import models
from django.utils import timezone
# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    img1 = models.ImageField(upload_to="upload", null=True)
    img2 = models.ImageField(upload_to="upload", blank=True)
    img3 = models.ImageField(upload_to="upload", blank=True)
    img4 = models.ImageField(upload_to="upload", blank=True)
    img5 = models.ImageField(upload_to="upload", blank=True)
    descripcion = models.TextField(null=True)
    fecha = models.DateField(default=timezone.now)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.titulo} ({self.autor})"
    def getImages(self):
        return [self.img1, self.img2,self.img3,self.img4,self.img5,]
