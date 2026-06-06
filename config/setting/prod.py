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
# ⚠️ کلید اصلی و امنیتی سرور (این را بعداً عوض کن یا از env بخوان)
SECRET_KEY = 'django-secure-production-key-change-this-sajad-hatami'

# در محیط پروداکشن حتماً باید False باشد تا خطاهای بک‌اند لو نرود
DEBUG = False

# تنظیم دقیق دامنه‌ها برای جلوگیری از حملات Host Header
ALLOWED_HOSTS = ['sajadhatami.ir', 'www.sajadhatami.ir']

# دیتابیس پروداکشن (هاست‌های سی‌پنل معمولاً از MySQL استفاده می‌کنند)
# اگر می‌خواهی روی هاست هم فعلاً از همان sqlite استفاده کنی، این بخش را دست نزن
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔒 تنظیمات سخت‌گیرانه امنیتی پروداکشن (Security Checklist)
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# اگر هاست شما SSL فعال دارد (https)، این دو خط را فعال کنید تا کوکی‌ها امن شوند
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True



# تنظیمات استاتیک و مدیا در پروداکشن
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'