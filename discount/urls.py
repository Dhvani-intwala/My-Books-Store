from django.urls import path
from . import views

urlpatterns = [
    path('discount/', views.book_discount_list, name='discounts'),
]