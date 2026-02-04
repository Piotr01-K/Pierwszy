from django.db import models

#  dodane Lesson 29 Task 10
class EmailNotification(models.Model):
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Email to {self.recipient_email}"
    
#  dodane Lesson 29 Task 12 
class LogEntry(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log {self.id} ({self.created_at})"
