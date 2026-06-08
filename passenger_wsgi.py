import os
import sys

# ۱. تنظیم مسیر پروژه
sys.path.insert(0, os.path.dirname(__file__))

# ۲. تنظیم فایل تنظیمات (Production)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.setting.prod')

# ۳. حل مشکل درایور MySQL
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

# ۴. راه‌اندازی اپلیکیشن WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()