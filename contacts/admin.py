from contacts.models import Contact, Contact_Urls
from django.contrib import admin


class ContactAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug' : ('name',)}
    pass
admin.site.register(Contact, ContactAdmin)
admin.site.register(Contact_Urls)
