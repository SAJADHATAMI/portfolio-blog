import os
from pathlib import Path
import pymysql

# حل مشکل MySQL در هاست‌های اشتراکی
pymysql.version_info = (1, 4, 6, 'final', 0)
pymysql.install_as_MySQLdb()

# مسیر اصلی پروژه: /home/lsaxuxzc/portfolio
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# امنیت
SECRET_KEY = 'django-secure-sajad-hatami-2026-key-replace-this'
DEBUG = False # حتما False باشد
ALLOWED_HOSTS = ['sajadhatami.ir', 'www.sajadhatami.ir']

# اپلیکیشن‌ها
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'blog',
    'contact',
    'core',
    'courses',
    'projects',
    'resume',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# دیتابیس MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lsaxuxzc_portfolio_db',
        'USER': 'lsaxuxzc_sajad',
        'PASSWORD': 'pD%R)U0@y}tI%%A&',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# محلی‌سازی
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True

# تنظیمات استاتیک (علت اصلی مشکل لود نشدن ظاهر سایت)
# تنظیمات استاتیک
STATIC_URL = '/static/'

# مسیر دقیق روی سرور برای جمع‌آوری فایل‌ها
STATIC_ROOT = '/home/lsaxuxzc/portfolio/staticfiles'

# مسیری که فایل‌های استاتیک خام پروژه تو در آن قرار دارد
STATICFILES_DIRS = [
    '/home/lsaxuxzc/portfolio/static',
]

# تنظیمات مدیا
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/lsaxuxzc/portfolio/media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# امنیت بیشتر (Security Checklist)
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True