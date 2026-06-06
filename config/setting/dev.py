#  تنظیمات مشترک
from pathlib import Path
import os

# با توجه به اینکه فایل یک پوشه عقب‌تر رفته، دو بار parent می‌گیریم تا به ریشه پروژه برسیم
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# برنامه های نصب شده
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    # my apps
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

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# محلی‌سازی و زمان
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tehran'  # تنظیم شده روی ساعت ایران
USE_I18N = True
USE_TZ = True

# تنظیمات استاتیک و مدیا مشترک
STATIC_URL = '/static/'

MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'












# تنظیمات اختصاصی
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
