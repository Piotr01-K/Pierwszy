from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import hello_world
from django.http import JsonResponse
from .tasks import multiply   # dodane Lesson 29 Task 2
from .tasks import log_timestamp   # dodane Lesson 29 Task 3
from django.http import HttpResponse   # dodane Lesson 29 Task 3
from .tasks import count_users  # dodane Lesson 29 Task 5
from django.contrib.auth.decorators import login_required   # dodane Lesson 29 Task 7
from django.http import HttpResponse   # dodane Lesson 29 Task 7
from .tasks import update_user_last_login    # dodane Lesson 29 Task 7
from .tasks import simulate_video_processing   # dodane Lesson 29 Task 8
from core.tasks import send_email_notification    # dodane Lesson 29 Task 10
from core.models import EmailNotification    # dodane Lesson 29 Task 10
from celery.result import AsyncResult   # dodane Lesson 29 Task 11
from core.tasks import long_running_task  # dodane Lesson 29 Task 11
from core.tasks import generate_users_csv   # dodane Lesson 29 Task 14
from django.conf import settings   # dodane Lesson 29 Task 14
from core.tasks import fetch_non_existing_url   # dodane Lesson 29 Task 15

# dodane Lesson 29 Task 1
@api_view(['GET'])
def trigger_hello_world(request):
    hello_world.delay()
    return Response({
        "message": "Zadanie hello_world zostało wysłane do Celery"
    })

def hello_view(request):
    hello_world.delay()
    return JsonResponse(
        {"message": "Zadanie hello_world zostało wysłane do Celery"}
    )
# dodane Lesson 29 Task 2
def multiply_view(request):
    result = None

    if request.method == "POST":
        a = int(request.POST.get("a"))
        b = int(request.POST.get("b"))

        task = multiply.delay(a, b)
        result = task.get(timeout=10)

    return render(request, "core/multiply.html", {"result": result})

# dodane Lesson 29 Task 3
def trigger_log_timestamp(request):
    log_timestamp.delay()
    return HttpResponse("Zapisano timestamp do pliku log.txt")

# dodane Lesson 29 Task 5
def count_users_view(request):
    count_users.delay()
    return HttpResponse("Zadanie count_users zostało uruchomione.")

# dodane Lesson 29 Task 7
@login_required
def trigger_update_last_login(request, user_id):
    update_user_last_login.delay(user_id)
    return HttpResponse(f"Updated last_login for user {user_id}")

# dodane Lesson 29 Task 8
def start_video_processing(request):
    simulate_video_processing.delay()
    return HttpResponse("Przetwarzanie wideo rozpoczęte!")

#  dodane Lesson 29 Task 10
def trigger_email_notification(request):
    email = EmailNotification.objects.create(
        recipient_email="test@example.com",
        subject="Test email",
        body="This is a simulated email."
    )

    send_email_notification.delay(email.id)

    return JsonResponse({
        "message": "Email sending started",
        "email_id": email.id
    })

# dodane Lesson 29 Task 11
def start_progress_task(request):
    task = long_running_task.delay()
    return JsonResponse({"task_id": task.id})

def task_status(request, task_id):
    result = AsyncResult(task_id)

    response = {
        "task_id": task_id,
        "state": result.state,
        "info": result.info,
    }

    return JsonResponse(response)

# dodane Lesson 29 Task 14
def start_users_csv(request):
    task = generate_users_csv.delay()
    return JsonResponse({
        "task_id": task.id,
        "status": "started"
    })

def task_result(request, task_id):
    result = AsyncResult(str(task_id))

    if result.state == "SUCCESS":
        file_path = result.result.get("file")
        return JsonResponse({
            "status": result.state,
            "download_url": settings.MEDIA_URL + file_path
        })

    return JsonResponse({
        "status": result.state
    })

# dodane Lesson 29 Task 15
def start_retry_task(request):
    task = fetch_non_existing_url.delay()
    return JsonResponse({
        "task_id": task.id,
        "status": "started"
    })