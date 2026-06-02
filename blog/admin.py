from multiprocessing.resource_tracker import register

from django.contrib import admin
from .models import Tag, Post, Category, Image
# Register your models here.


admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Image)
