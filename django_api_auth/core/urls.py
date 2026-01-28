from django.urls import path
from .views import trigger_hello_world
from .views import hello_view
from .views import multiply_view   # dodane Lesson 29 Task 2

# dodane Lesson 29 Task 1
urlpatterns = [
    path('hello/', trigger_hello_world, name='hello-world'),
    path("hello/", hello_view, name="core-hello"),
    path("multiply/", multiply_view),    # dodane Lesson 29 Task 2
]
