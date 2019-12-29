from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ModelBlog

def home(requests):
    # data = {'correo': 'pedro@gmail.com'}
    data = ModelBlog.objects.all()
    return render(requests, 'blog/blog.html', {'data': data})
    # return HttpResponse('<h1> hola mi blog desde django </h1>')

def index(requests):
    return redirect('blog')
