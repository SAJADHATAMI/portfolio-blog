"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# my
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap  # ۱. ایمپورت ویوی پیش‌فرض سایت‌مپ جنگو
from core.sitemaps import StaticViewSitemap, BlogSitemap, ProjectSitemap, CourseSitemap  # ۲. ایمپورت کلاس‌هایی که ساختی

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
    'projects': ProjectSitemap,
    'courses': CourseSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('projects/', include('projects.urls')),
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),

    # ۴. مسیر رسمی فایل XML برای موتورهای جستجو
    path('sitemap.xml',
         sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'), ]

# ========== سرویس فایل‌های استاتیک و مدیا در حالت توسعه ==========
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
