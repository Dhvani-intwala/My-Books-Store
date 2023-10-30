from django import forms
from .models import Subscribers, MailMessage


class SubscribersForm(forms.ModelForm):
    """Form for adding email to newsletter subscribers"""
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'id': 'newsletter_email', }), label="Enter your email:")

    class Meta:
        model = Subscribers
        fields = ['email', ]