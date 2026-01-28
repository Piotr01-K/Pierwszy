from celery import shared_task

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
