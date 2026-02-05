from django.urls import path
from .views import trigger_hello_world
from .views import hello_view
from .views import multiply_view   # dodane Lesson 29 Task 2
from .views import trigger_log_timestamp   # dodane Lesson 29 Task 3
from . import views   # dodane Lesson 29 Task 5
from .views import trigger_update_last_login   # dodane Lesson 29 Task 7
from .views import start_video_processing   # dodane Lesson 29 Task 8
from .views import start_progress_task, task_status   # dodane Lesson 29 Task 11

# dodane Lesson 29 Task 1
urlpatterns = [
    path('hello/', trigger_hello_world, name='hello-world'),
    path("hello/", hello_view, name="core-hello"),
    path("multiply/", multiply_view),    # dodane Lesson 29 Task 2
    path("log-timestamp/", trigger_log_timestamp),   # dodane Lesson 29 Task 3
    path("count-users/", views.count_users_view),   # dodane Lesson 29 Task 5
    path("update-last-login/<int:user_id>/", trigger_update_last_login, name="update_last_login"),   # dodane Lesson 29 Task 7
    path("video/start/", start_video_processing, name="start_video_processing"),   # dodane Lesson 29 Task 8
    path("send-email/", views.trigger_email_notification),  # dodane Lesson 29 Task 10
    path("start-progress-task/", start_progress_task, name="start_progress_task"),   # dodane Lesson 29 Task 11
    path("task-status/<str:task_id>/", task_status, name="task_status"),   # dodane Lesson 29 Task 11
    path("start-users-csv/", views.start_users_csv),   # dodane Lesson 29 Task 14
    path("task-result/<uuid:task_id>/", views.task_result),   # dodane Lesson 29 Task 14
]
