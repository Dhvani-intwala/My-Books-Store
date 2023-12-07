from django.test import TestCase, Client
from django.urls import reverse
from .forms import ContactForm


class ContactUsViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contact_us_view(self):
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contactus/contact_us.html')
     
    def test_contact_us_form_submission(self):
        data = {
            'name': 'User',
            'email': 'user@example.com',
            'phone': '017642454232',
            'message': 'Test message'
        }
        response = self.client.post(reverse('contact_us'), data)
        self.assertEqual(response.status_code, 302)

    def test_invalid_contact_us_form_submission(self):
        invalid_data = {}
        response = self.client.post(reverse('contact_us'), invalid_data)
        self.assertEqual(response.status_code, 200)