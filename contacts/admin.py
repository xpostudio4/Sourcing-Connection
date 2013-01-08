from contacts.models import Contact
from django.contrib import admin


class ContactAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug' : ('name',)}
    pass
admin.site.register(Contact, ContactAdmin)
