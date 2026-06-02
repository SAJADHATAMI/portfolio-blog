
from django.db import models
from core.models import Skill
# Create your models here.

class Coach(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100, unique=True)
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    coach = models.ForeignKey(Coach, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='courses/images/', blank=True, null=True)
    certificate_image = models.ImageField(upload_to='courses/images/', blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.title