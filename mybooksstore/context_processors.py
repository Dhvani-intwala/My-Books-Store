
from newsletter.forms import SubscribersForm


def add_subscription_form_to_context(request):
    """Method to return subscription form as context"""
    return {
        'add_subscriber_form': SubscribersForm
    }


