from companies.models import Company, Office, Management, Funding, \
	AccessCompanyProfile, Competitors, ContactCompany, CompanyRating,\
	ProfileCompletion, CompanyLink, Acquisition, Certification, Customer,\
	Award, CompanyLink, ManagementPicture
from fileupload.models import Picture
from django.contrib import admin
from wysihtml5.admin import AdminWysihtml5TextFieldMixin

class PictureInline(admin.StackedInline):
    model = Picture
    extra = 3
    exclude = ["slug"]

class CompanyAdmin(AdminWysihtml5TextFieldMixin, admin.ModelAdmin):
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

class AcquisitionAdmin(admin.ModelAdmin):
	pass

class CompanyLinkAdmin(admin.ModelAdmin):
	pass

class AccessCompanyProfileAdmin(admin.ModelAdmin):
	pass

class ContactCompanyAdmin(admin.ModelAdmin):
	pass

class CustomerAdmin(admin.ModelAdmin):
	pass

class AwardAdmin(admin.ModelAdmin):
	pass

class CompanyRatingAdmin(admin.ModelAdmin):
	pass

class ManagementPictureAdmin(admin.ModelAdmin):
	pass

admin.site.register(ProfileCompletion)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyRating, CompanyRatingAdmin)
admin.site.register(ContactCompany, ContactCompanyAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(Certification)
admin.site.register(Competitors,CompetitorsAdmin)
admin.site.register(Acquisition,AcquisitionAdmin)
admin.site.register(CompanyLink,CompanyLinkAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Award,AwardAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Funding, FundingAdmin)
admin.site.register(ManagementPicture, ManagementPictureAdmin)
admin.site.register(AccessCompanyProfile, AccessCompanyProfileAdmin)