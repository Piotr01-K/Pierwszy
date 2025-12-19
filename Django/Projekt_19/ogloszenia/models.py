#   dodane  w ramach lesson 21 task 1
from django.db import models
from django.utils import timezone   #  dodane w ramach Lesson 21 Task 8

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#    dodane w ramach lesson 21 task 7
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='articles'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)    #  dodałem w ramach lesson 21 task 8

    def __str__(self):
        return self.title