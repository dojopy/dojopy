from django.db import models
from django.utils import timezone


class ModelSaludo(models.Model):
    mensaje = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return '{} - {}'.format(self.mensaje, self.nombre)


class ModelBlog(models.Model):
    title = models.CharField(max_length=200, default="")
    author = models.CharField(max_length=200, default="")
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    texto_breve = models.CharField(max_length=200, default="")
    url_image = models.CharField(max_length=200, default="")

    def __str__(self):
        return '{} - {}'.format(self.author, self.created_date)


class ModelContact(models.Model):
    created = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200, default="")
    correo = models.EmailField(max_length=200, default="")
    mensaje = models.CharField(max_length=200, default="")

    def __str__(self):
        return '{} {} {}'.format(
                        self.created,
                        self.correo,
                        self.name )
