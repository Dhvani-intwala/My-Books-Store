from django.views.generic import CreateView
from django.shortcuts import render, redirect
from newsletter.forms import SubscribersForm
from . forms import MailMessageForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from newsletter.models import Subscribers
from django.core.mail import send_mail
from django_pandas.io import read_frame


class SubscribeToNewsletter(CreateView):
    """A view that provides a form for users to subscribe for newsletter"""
    model = Subscribers
    form_class = SubscribersForm
    template_name = "base.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['path'] = self.kwargs.get('path')
        return kwargs

    def post(self, request, *args, **kwargs):
        """Override post method"""
        if request.method == 'POST':

            subscribe_form = SubscribersForm(request.POST, request.FILES)

            if subscribe_form.is_valid():
                email = subscribe_form.cleaned_data['email']
                subscription = Subscribers(email=email)
                subscription.save()
                messages.success(
                    request, 'Thank you for your subscription!',
                    extra_tags="form_success")
                return HttpResponseRedirect(request.POST.get(
                    'newsletter_submit_btn', '') + '#newsletter')
            else:
                messages.error(request, subscribe_form.errors['email'],
                               extra_tags="form_errors")
                return HttpResponseRedirect(request.POST.get(
                    'newsletter_submit_btn', '') + '#newsletter')

        subscribe_form = SubscribersForm()
        return render(request, 'base.html',
                      {'add_subscriber_form': subscribe_form, })


def mail_letter(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        mailMessage_form = MailMessageForm(request.POST)
        if mailMessage_form.is_valid():
            mailMessage_form.save()
            title = mailMessage_form.cleaned_data.get('title')
            message = mailMessage_form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to the Mail List')
            return redirect('mail-letter')
    else:
        mailMessage_form = MailMessageForm()
    return render(request, 'newsletter/mailmessage.html',
                            {'add_mailmeassage': mailMessage_form, })