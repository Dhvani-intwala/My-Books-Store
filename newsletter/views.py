from django.shortcuts import render, redirect
from .forms import SubscribersForm
from django.contrib import messages


def SubscribeToNewsletter(request):
    """A view that provides a form for users to subscribe for newsletter"""
  
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your subscription!')
            return redirect('base')
    else:
        form = SubscribersForm()
    template_name = "base.html"
    context = {
        'newsletterform': newsletterform,
    }

    return render(request, template_name, context)

