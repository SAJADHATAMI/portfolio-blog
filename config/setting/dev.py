from config.settings import * # ارث‌بری تمام تنظیمات فایل مشترک

# کلید سکرت موقت برای روی سیستم خودت
SECRET_KEY = 'django-insecure--kjgi!^6lv5gc79*ri7wpa!q8ygns@en&rkikbdd%l3o%r@s^o'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# دیتابیس محلی سبک sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}





# پوشه‌ای که فایل‌های استاتیک پروژه در آن قرار می‌گیرند (جمع‌آوری شده)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# پوشه‌هایی که جنگو در آنها فایل‌های استاتیک را جستجو می‌کند (برای توسعه)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


# مسیر ذخیره‌سازی فایل‌های مدیا روی دیسک
MEDIA_ROOT = BASE_DIR / 'media'
