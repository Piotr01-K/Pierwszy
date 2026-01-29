import os
from celery import Celery

# Informujemy Celery, gdzie są ustawienia Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Tworzymy instancję aplikacji Celery
app = Celery('config')

# Wczytujemy konfigurację z settings.py (prefiks CELERY_)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatyczne wykrywanie plików tasks.py
app.autodiscover_tasks()
