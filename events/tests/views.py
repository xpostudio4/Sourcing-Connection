from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import unittest, timezone

from events.models import Event 
from events.forms import EventForm
from events.views import *

class EventPageViewTest(TestCase):

    def test_index(self):
        resp = self.client.get('/events/')
        self.assertEqual(resp.status_code, 200)

    def test_root_url_shows_all_events(self):
        # set up some events
        user = User.objects.create(username="john")
        event1 = Event(
            title='PyCon 2013', 
            slug='pycon-2013', 
            description='The most advanced conference about Python',
            where='Santa Clara, California',
            posted_by=user,
            datetime = timezone.now())
        event1.save()
        event2 = Event(
            title='PyData 2013', 
            slug='pydata-2013', 
            description='The most advanced conference about Python and Data Analysis',
            where='Santa Clara, California',
            posted_by=user,
            datetime = timezone.now())
        
        event2.save()

        response = self.client.get('/events/')

        self.assertTemplateUsed(response, 'event_list.html')

        self.assertIn(event1.title, response.content)
        self.assertIn(event1.slug, response.content)
        self.assertIn(event1.description, response.content)
        self.assertIn(event2.title, response.content)


