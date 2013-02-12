from companies.models import Company, Office, Management, Funding, AccessCompanyProfile, Competitors, ContactCompany, CompanyRating
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

class ContactCompanyAdmin(admin.ModelAdmin):
	pass

class CompanyRatingAdmin(admin.ModelAdmin):
	pass

admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyRating, CompanyRatingAdmin)
admin.site.register(ContactCompany, ContactCompanyAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(Competitors,CompetitorsAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Funding, FundingAdmin)
admin.site.register(AccessCompanyProfile,AccessCompanyProfileAdmin)
