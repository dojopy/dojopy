from django.db import models
from django.utils import timezone

# Create your models here.


class ModelBlog(models.Model):
    title = models.CharField(max_length=200, default="")
    author = models.CharField(max_length=200, default="")
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    texto_breve = models.CharField(max_length=200, default="")
    url_image = models.CharField(max_length=200, default="")

    def __str__(self):
        return '{} - {}'.format(self.author, self.created_date)
