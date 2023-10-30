from django.urls import path
from . import views

urlpatterns = [
    path('', views.SubscribeToNewsletter.as_view(), name='newsletter'),
    path('mail-letter/', views.mail_letter, name='mail-letter'),
]