from django.urls import path
from . import views

urlpatterns = [
    path('', views.SubscribeToNewsletter.as_view(), name='newsletter'),
]