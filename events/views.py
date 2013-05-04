from django.views.generic import DetailView, ListView, UpdateView, CreateView, ListView
from events.forms import EventForm
from events.models import Event

class EventListView(ListView):
	model = Event 
	template_name = 'event_list.html'

class EventNewView(CreateView):
	form_class = EventForm
	template_name = 'event_form.html'