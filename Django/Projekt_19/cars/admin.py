from django.contrib import admin
from .models import Car

#   admin.site.register(Car)   #  zahashowane przy Lesson 23 task 2 (zapis zastąpiony lepszym)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'brand', 'model', 'year', 'is_available')    # zmiana: dodanie 'full_name' w ramach Lesson 23 task 6
    search_fields = ('brand', 'model')    # dodane w ramach Lesson 23 task 3
    list_filter = ('is_available', 'year')    # dodane w ramach Lesson 23 task 4
    ordering = ('-year',)

    readonly_fields = ('year',)   # dodane w ramach Lesson 23 task 7 (pole tylko do odczytu)

        # dodane w ramach Lesson 23 task 6
    @admin.display(description="Pełna nazwa")
    def full_name(self, obj):
        return f"{obj.brand} {obj.model}"

    full_name.short_description = "Pełna nazwa"