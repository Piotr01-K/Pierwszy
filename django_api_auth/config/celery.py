import os
from celery import Celery
from kombu import Queue  # dodane Lesson 29 Task 18

# Informujemy Celery, gdzie są ustawienia Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Tworzymy instancję aplikacji Celery
app = Celery('config')

# Wczytujemy konfigurację z settings.py (prefiks CELERY_)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatyczne wykrywanie plików tasks.py
app.autodiscover_tasks()

# dodane Lesson 29 Task 18
app.conf.task_queues = (
    Queue("default"),
    Queue("priority_queue"),
)

app.conf.task_default_queue = "default"