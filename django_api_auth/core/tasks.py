import time    # dodane Lesson 29 Task 8
from celery import shared_task
from datetime import datetime   # dodane Lesson 29 Task 3
from pathlib import Path   # dodane Lesson 29 Task 3
from django.contrib.auth.models import User  # dodane Lesson 29 Task 5
from django.contrib.auth import get_user_model   # dodane Lesson 29 Task 7
from django.utils import timezone   # dodane Lesson 29 Task 7

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
    now = timezone.now()
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{now}\n")
    print(f"Logged timestamp: {now}")

# dodane Lesson 29 Task 5
@shared_task
def count_users():
    User = get_user_model()
    count = User.objects.count()
    print(f"Liczba użytkowników w bazie: {count}")
    return count

# dodane Lesson 29 Task 6
@shared_task
def update_user_last_login(user_id):
    User = get_user_model()

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        print(f"User with id={user_id} does not exist")
        return

    user.last_login = timezone.now()
    user.save(update_fields=["last_login"])

    print(f"Updated last_login for user id={user_id}")

# dodane Lesson 29 Task 8
@shared_task
def simulate_video_processing():
    print("Start przetwarzania wideo...")
    time.sleep(15)
    print("Zakończono przetwarzanie wideo.")