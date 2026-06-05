from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from projects.models import STATUS_CHOICES
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    def __str__(self): return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class BlogCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    def __str__(self): return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    blogCategory = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    cover_image = models.ImageField(
        upload_to='posts/images/',
        blank=True, null=True
    )
    short_description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

        def get_absolute_url(self):
            return reverse('blog_detail', kwargs={'slug': self.slug})

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='posts/images/', blank=True)
    caption = models.TextField(blank=True)
    def __str__(self):
        return self.caption or f"Image for {self.post.title}"
