from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Event)
