from django.shortcuts import render, redirect
from .forms import SubscribersForm
from django.contrib import messages


def SubscribeToNewsletter(request):
    """A view that provides a form for users to subscribe for newsletter"""
  
    if request.method == 'POST':
        newsletterform = SubscribersForm(request.POST)
        if newsletterform.is_valid():
            newsletterform.save()
            messages.success(request, 'Thank you for your subscription!')
            return redirect('base')
    else:
        newsletterform = SubscribersForm()
    template_name = "base.html"
    context = {
        'newsletterform': newsletterform,
    }

    return render(request, template_name, context)

