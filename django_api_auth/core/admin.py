from django.contrib import admin
from .models import LogEntry   # dodane Lesson 29 Task 12

#   dodane Lesson 29 Task 10
from core.models import EmailNotification
from .models import ScrapedPage   # dodane Lesson 29 Task 13

admin.site.register(EmailNotification)

# dodane Lesson 29 Task 12
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "message")
    list_filter = ("created_at",)

# dodane Lesson 29 Task 13
@admin.register(ScrapedPage)
class ScrapedPageAdmin(admin.ModelAdmin):
    list_display = ("url", "title", "scraped_at")
    list_filter = ("scraped_at",)