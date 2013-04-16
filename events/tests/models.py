from companies.models import Company

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import unittest, timezone

from events.models import Event 
from events.forms import EventForm



class EventModelTest(TestCase):
    def test_creating_new_event_and_saving_it_to_the_database(self):
        # Test creating a new event object.
        user = User.objects.create(username="fulano")
        company = Company()
        event = Event()
        event.title = "Test Driven Development with Django"
        event.slug = "test-driven-development-with-django"
        event.description = "Fantastic way to develop web applications with less bugs and stress"
        event.where = "Avenida Mella No.444, Plaza Hispaniola, Suite 101"
        event.company = company
        event.posted_by = user
        event.datetime = timezone.now()

        #check if our event can be safe to the DB
        event.save()

        #check if our event is created 

        all_events_in_database = Event.objects.all()
        self.assertEquals(len(all_events_in_database), 1)
        only_event_in_database = all_events_in_database[0]
        self.assertEquals(only_event_in_database, event)

