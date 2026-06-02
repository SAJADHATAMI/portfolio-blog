from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile')
    short_bio = models.TextField(blank=True)
    about = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    discord = models.URLField(blank=True)
    bale = models.URLField(blank=True)
    resume = models.FileField(upload_to='resumes', blank=True)
    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percent = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    priority = models.IntegerField(unique=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['priority']


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100)
    site_domain = models.URLField()
    logo = models.ImageField(upload_to='sitesets', blank=True)
    favicon = models.ImageField(upload_to='sitesets', blank=True)
    copyright_text = models.TextField(blank=True)
    google_analytics_id = models.CharField(max_length=300,blank=True)
    def __str__(self):
        return self.site_name