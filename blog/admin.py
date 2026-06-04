from multiprocessing.resource_tracker import register

from django.contrib import admin
from .models import Tag, Post, BlogCategory, Image
# Register your models here.


admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(BlogCategory)
admin.site.register(Image)
