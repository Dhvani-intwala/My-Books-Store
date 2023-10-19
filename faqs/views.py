from django.shortcuts import render
from .models import FAQ

# Create your views here.


def FAQViews(request):

    template_name = 'faqs/faqs.html'
    context = {
        'faq': '',
         
    }
    return render(request, template_name, context)

