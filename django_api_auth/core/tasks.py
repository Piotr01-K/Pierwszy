from celery import shared_task
from datetime import datetime   # dodane Lesson 29 Task 3
from pathlib import Path   # dodane Lesson 29 Task 3
from django.contrib.auth.models import User  # dodane Lesson 29 Task 4

# dodane Lesson 29 Task 1
@shared_task
def hello_world():
    print("Hello from Celery!")

# dodane Lesson 29 Task 2
@shared_task
def multiply(a, b):
    result = a * b
    print(f"Multiply result: {result}")
    return result

# dodane Lesson 29 Task 3
@shared_task
def log_timestamp():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    base_dir = Path(__file__).resolve().parent.parent
    log_file = base_dir / "log.txt"

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{now}\n")

    return now

# dodane Lesson 29 Task 4
@shared_task
def count_users():
    count = User.objects.count()
    print(f"Liczba użytkowników w bazie: {count}")