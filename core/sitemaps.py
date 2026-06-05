from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post # فرض بر اینکه مدل پست بلاگت اینجاست
from projects.models import Project  # ایمپورت مدل پروژه
from courses.models import Course    # ایمپورت مدل دوره

class StaticViewSitemap(Sitemap):
    priority = 1.0         # اولویت بالا برای صفحه اصلی
    changefreq = 'daily'   # نرخ تغییرات

    def items(self):
        return ['home']    # نام یو‌آر‌ال صفحه اصلی

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return Post.objects.exclude(status=0) # فقط پست‌های منتشر شده

    # متد get_absolute_url باید روی مدل Post شما تعریف شده باشد تا آدرس دقیق هر پست را برگرداند


class ProjectSitemap(Sitemap):
    priority = 0.9          # اولویت بالاتر برای پروژه‌های نمونه کار
    changefreq = 'monthly'  # پروژه‌ها معمولاً دیر به دیر تغییر می‌کنند

    def items(self):
        return Project.objects.exclude(status=0) # فرض بر اینکه فیلد status داری

class CourseSitemap(Sitemap):
    priority = 0.9
    changefreq = 'weekly'

    def items(self):
        return Course.objects.all() # واکشی تمام دوره‌ها