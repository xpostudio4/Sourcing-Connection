from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import unittest, timezone

from events.models import Event 
from events.forms import EventForm


class EventFormTest(TestCase):
    def test_event_forms(self):
        user = User.objects.create(username="john")
        event1 = Event(
            title='PyCon 2013', 
            slug='pycon-2013', 
            description='The most advanced conference about Python',
            where='Santa Clara, California',
            posted_by=user,
            datetime = timezone.now())
        event1.save()
        form = EventForm()
