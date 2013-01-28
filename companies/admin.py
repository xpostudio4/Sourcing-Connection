from companies.models import Company, Office, Management, Funding 
from fileupload.models import Picture
from django.contrib import admin

class PictureInline(admin.StackedInline):
    model = Picture
    extra = 3
    exclude = ["slug"]

class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    inlines = [PictureInline]

class OfficeAdmin(admin.ModelAdmin):
    pass

class ManagementAdmin(admin.ModelAdmin):
	pass

class FundingAdmin(admin.ModelAdmin):
	pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Funding, FundingAdmin)
