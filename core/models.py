from django.db import models

class TelegramLog(models.Model):
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message at {self.sent_at}"
