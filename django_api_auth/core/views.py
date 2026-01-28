from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import hello_world
from django.http import JsonResponse
from .tasks import multiply   # dodane Lesson 29 Task 2

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