from django.db import models

# Create your models here.
from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    degree_title = models.CharField(max_length=150)
    field_of_study = models.CharField(max_length=150)
    institution = models.CharField(max_length=150)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    technologies = models.ManyToManyField(Technology, blank=True)

    def __str__(self):
        return f"{self.degree_title} - {self.institution}"


class Experience(models.Model):
    job_title = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    technologies = models.ManyToManyField(Technology, blank=True)

    def __str__(self):
        return f"{self.job_title} - {self.company}"
