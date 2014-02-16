"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User

from app.utils import parse_inbound
from app.models import Item


class SimpleTest(TestCase):
    def setUp(self):
        with open(settings.ROOT_PATH + '/../app/fixtures/inbound.json') as f:
            self.data = f.read()

        self.user = User.objects.create(username='tzangms', email='tzangms@gmail.com')

    def test_profile_signal(self):
        self.assertEqual(self.user.profile.nickname, 'tzangms')


    def test_parse_inbound(self):

        email, items = parse_inbound(self.data)

        self.assertEqual(email, 'tzangms@gmail.com')
        self.assertEqual(len(items), 4)

    def test_model(self):
        email, items = parse_inbound(self.data)

        user = User.objects.get(email=email)

        for item in items:
            Item.objects.create(user=user, text=item).save()

        items_count = Item.objects.filter(user=user).count()
        self.assertEqual(items_count, 4)

    def test_view(self):
        resp = self.client.post('/inbound/', data=self.data, content_type='application/json')

        self.assertEqual(resp.status_code, 200)

        items_count = Item.objects.filter(user__username='tzangms').count()
        self.assertEqual(items_count, 4)
