import unittest
from django.test import TestCase, Client
from django.urls import reverse
from contactus.views import contactUs
from contactus.forms import ContactForm


class ContactUsViewTest(unittest.TestCase):
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
            'subject': 'subject',
            'message': 'Test message'
        }
        form_data = ContactForm(data = data)
        response = self.client.post(reverse('contact_us'), form_data)
        self.assertEqual(response.status_code, 302)

    def test_invalid_contact_us_form_submission(self):
        invalid_data = {
             'name': '',
            'email': '',
            'phone': '',
            'message': '',
            'subject': '',
        }
        invalid_form_data = ContactForm(data = invalid_data)
        response = self.client.post(reverse('contact_us'), invalid_form_data)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()