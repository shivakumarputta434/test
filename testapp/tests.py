from django.test import TestCase
from testapp.models import Student
from testapp.views import jointable,home
from django.urls import reverse,resolve
from django.test import SimpleTestCase

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_url_resolved(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,home)

