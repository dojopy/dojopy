from django.shortcuts import render
from django.http import HttpResponse
from .models import ModelSaludo, ModelBlog

# Create your views here.

def home(request):
    obj = ModelSaludo.objects.all()
    obj = obj.values()
    # return HttpResponse('<h1> ¿hola te gusta mi pagina? </h1>')
    return render(request, 'hello.html', {'data': obj})


def blog(request):
    obj = ModelBlog.objects.all()
    obj = obj.values()
    return render(request, 'blog.html', {'data': obj})
