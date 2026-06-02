from django.contrib import admin
from .models import Profile, Skill, SiteSettings

# Register your models here.

admin.site.register(SiteSettings)

admin.site.register(Profile)

admin.site.register(Skill)


