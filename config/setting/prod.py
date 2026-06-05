from config.settings import *

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