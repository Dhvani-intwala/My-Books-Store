from django.urls import path
from . import views

urlpatterns = [
    path('', views.FAQViews, name='faqsview')
]