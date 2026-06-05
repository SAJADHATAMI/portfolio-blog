from django.db import models
from django.urls import reverse

from core.models import Skill
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


STATUS_CHOICES = [
    (0, 'Draft'),
    (1, 'In Progress'),
    (2, 'Completed'),
    (3, 'Archived'),
]

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    skills = models.ManyToManyField(Skill)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/images/', blank=True)
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=0
    )


    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})