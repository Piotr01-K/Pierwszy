from django.contrib import admin
from .models import Car

#   admin.site.register(Car)   #  zahashowane przy Lesson 23 task 2 (zapis zastąpiony lepszym)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'is_available')
    search_fields = ('brand', 'model')    # dodane w ramach Lesson 23 task 3
    list_filter = ('is_available', 'year')    # dodane w ramach Lesson 23 task 4
    ordering = ('-year',)