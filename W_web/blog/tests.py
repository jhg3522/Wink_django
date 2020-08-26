from django.test import TestCase,Client
from bs4 import BeautifulSoup
from .models import Post,Category
from django.utils import timezone
from django.contrib.auth.models import User

def create_category(name='life', description=None):
    category, is_created = Category.objects.get_or_create(
        name=name,
        description=description
    )

    return category


class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title

        self.assertEqual(title.text,'Blog')
