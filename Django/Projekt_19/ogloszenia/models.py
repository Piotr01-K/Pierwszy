#   dodane  w ramach lesson 21 task 1
from django.db import models

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

    def __str__(self):
        return self.title