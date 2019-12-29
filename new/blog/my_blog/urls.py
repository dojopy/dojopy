from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.home, name='blog'),
    path('', views.index, name='index'),

]
