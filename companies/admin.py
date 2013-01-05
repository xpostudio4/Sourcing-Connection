from companies.models import Company, Office
from django.contrib import admin


class CompanyAdmin(admin.ModelAdmin):
    pass
class OfficeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Company, CompanyAdmin)
admin.site.register(Office, OfficeAdmin)
