from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import ContactMessage

class ContactUsViewTest(TestCase):
    def test_contact_form_submission(self):
        # Test POST request with valid data
        response = self.client.post(reverse('contact_us'), {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'phone': '1234567890',
            'subject': 'Test Subject',
            'message': 'Test Message',
        })

