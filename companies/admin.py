from companies.models import Company, Office, Management, Funding, AccessCompanyProfile, Competitors
from fileupload.models import Picture
from django.contrib import admin

class PictureInline(admin.StackedInline):
    model = Picture
    extra = 3
    exclude = ["slug"]

class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    inlines = [PictureInline]

class CompetitorsAdmin(admin.ModelAdmin):
	pass

class OfficeAdmin(admin.ModelAdmin):
    pass

class ManagementAdmin(admin.ModelAdmin):
	pass

class FundingAdmin(admin.ModelAdmin):
	pass

class AccessCompanyProfileAdmin(admin.ModelAdmin):
	pass

admin.site.register(Company, CompanyAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(Competitors,CompetitorsAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Funding, FundingAdmin)
admin.site.register(AccessCompanyProfile,AccessCompanyProfileAdmin)
