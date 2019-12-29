from django.contrib import admin
from .models import ModelSaludo, ModelBlog, ModelContact
# Register your models here.

admin.site.register(ModelSaludo)
admin.site.register(ModelBlog)
admin.site.register(ModelContact)
