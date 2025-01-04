from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class MyViewTestCase(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'index.html')
