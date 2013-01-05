from contacts.models import Contact
from django.contrib import admin


class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)
