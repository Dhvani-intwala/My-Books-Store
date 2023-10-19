from django.db import models

# Create your models here.


class Subscribers(models.Model):
    """Model for Subscription object"""
    email = models.EmailField(unique=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class MailMessage(models.Model):
    """Model for mail message object"""

    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title