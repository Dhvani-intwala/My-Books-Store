from django import forms
from .models import Subscribers, MailMessage


class SubscribersForm(forms.ModelForm):
    """Form for adding email to newsletter subscribers"""
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'id': 'newsletter_email', }), label="Enter your email:")

    class Meta:
        model = Subscribers
        fields = ['email', ]


class MailMessageForm(forms.ModelForm):
    """Form for adding email to newsletter subscribers"""
    title = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'title_email', }), label="Title")
    message = forms.CharField(widget=forms.Textarea(
        attrs={'id': 'message_mail', }), label="Message")

    class Meta:
        model = MailMessage
        fields = '__all__'