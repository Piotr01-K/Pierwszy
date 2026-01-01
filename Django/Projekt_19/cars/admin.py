from django.contrib import admin, messages   # dodane "messages" w ramach Lesson 23 task 8
from .models import Car

#   admin.site.register(Car)   #  zahashowane przy Lesson 23 task 2 (zapis zastąpiony lepszym)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'brand', 'model', 'year', 'is_available')    # zmiana: dodanie 'full_name' w ramach Lesson 23 task 6
    search_fields = ('brand', 'model')    # dodane w ramach Lesson 23 task 3
    list_filter = ('is_available', 'year')    # dodane w ramach Lesson 23 task 4
    ordering = ('-year',)

    #   readonly_fields = ('year',)   # dodane w ramach Lesson 23 task 7 (pole tylko do odczytu), ale zahashowane przy task 8

    actions = ['mark_as_unavailable']    # dodane w ramach Lesson 23 task 8 (akcja)
    
        # dodane w ramach Lesson 23 task 6
    @admin.display(description="Pełna nazwa")
    def full_name(self, obj):
        return f"{obj.brand} {obj.model}"

    full_name.short_description = "Pełna nazwa"

    #  dodane w ramach Lesson 23 task 7 (edytowalność year)
    def get_readonly_fields(self, request, obj=None):
        """
        - przy DODAWANIU (obj=None): year jest edytowalne
        - przy EDYCJI (obj istnieje): year jest tylko do odczytu
        """
        if obj:  # edycja istniejącego samochodu
            return ('year',)
        return ()

    # dodane w ramach Lesson 23 task 8 (nowa akcja)
    def mark_as_unavailable(self, request, queryset):
        updated = queryset.update(is_available=False)

        self.message_user(request, f"Oznaczono {updated} samochodów jako niedostępne.",
            messages.SUCCESS
        )

    mark_as_unavailable.short_description = "Oznacz jako niedostępne"