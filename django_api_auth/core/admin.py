from django.contrib import admin
from .models import LogEntry   # dodane Lesson 29 Task 12

#   dodane Lesson 29 Task 10
from core.models import EmailNotification

admin.site.register(EmailNotification)

# dodane Lesson 29 Task 12
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "message")
    list_filter = ("created_at",)
