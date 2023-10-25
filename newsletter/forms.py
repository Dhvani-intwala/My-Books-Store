from django import forms
from .models import Subscribers, MailMessage


class SubscribersForm(forms.ModelForm):
    """Form for adding email to newsletter subscribers"""
    class Meta:
        model = Subscribers
        fields = ['email',]