#post\models.py
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    titulo         = models.CharField(max_length=255)
    subtitulo      = models.CharField(max_length=255)
    contenido      = RichTextField(null=True)
    autor          = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True, auto_now=False)
    imagen         = models.ImageField(upload_to='galeria')

class Interes(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Post, on_delete=models.CASCADE)
    fecha_interes = models.DateTimeField(auto_now_add=True)


