import time    # dodane Lesson 29 Task 8
from celery import shared_task
from datetime import datetime   # dodane Lesson 29 Task 3
from pathlib import Path   # dodane Lesson 29 Task 3
from django.contrib.auth.models import User  # dodane Lesson 29 Task 5
from django.contrib.auth import get_user_model   # dodane Lesson 29 Task 7
from django.utils import timezone   # dodane Lesson 29 Task 7
from core.models import EmailNotification   # dodane Lesson 29 Task 10
import time   #  dodane Lesson 29 Task 11
from celery import shared_task  #  dodane Lesson 29 Task 11
from .models import LogEntry   # dodane Lesson 29 Task 12
from datetime import timedelta   # dodane Lesson 29 Task 12
import requests   # dodane Lesson 29 Task 13
from bs4 import BeautifulSoup   # dodane Lesson 29 Task 13
from .models import ScrapedPage   # dodane Lesson 29 Task 13

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

# dodane Lesson 29 Task 10
@shared_task
def send_email_notification(email_notification_id):
    try:
        email = EmailNotification.objects.get(id=email_notification_id)
    except EmailNotification.DoesNotExist:
        return f"EmailNotification {email_notification_id} does not exist"

    # symulacja wysyłki maila
    time.sleep(5)

    email.sent_at = timezone.now()
    email.save()

    return f"Email sent to {email.recipient_email}"

# dodane Lesson 29 Task 11
@shared_task(bind=True)
def long_running_task(self):
    total = 100

    for i in range(1, total + 1):
        time.sleep(0.1)

        self.update_state(
            state="PROGRESS",
            meta={
                "current": i,
                "total": total,
                "percent": int(i / total * 100),
            },
        )

    return {"current": total, "total": total, "percent": 100}

# dodane Lesson 29 Task 12
@shared_task
def delete_old_logs():
    cutoff_date = timezone.now() - timedelta(days=90)

    deleted_count, _ = LogEntry.objects.filter(
        created_at__lt=cutoff_date
    ).delete()

    return f"Deleted {deleted_count} old log entries"

# dodane Lesson 29 Task 13
@shared_task
def scrape_example_title():
    url = "https://example.com"

    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string.strip()

    ScrapedPage.objects.create(
        url=url,
        title=title
    )

    return title

