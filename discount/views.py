from django.shortcuts import render
from .models import Book_discount


def book_discount_list(request):
    discount = Book_discount.objects.all()
    return render(request, 'discount/discounts.html', {'discount': discount})
