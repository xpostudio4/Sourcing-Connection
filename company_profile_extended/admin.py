from company_profile_extended.models import *
from django.contrib import admin

class ExpertiseAdmin(admin.ModelAdmin):
	exclude = ["slug"]

class VerticalAdmin(admin.ModelAdmin):
	exclude = ["slug"]


admin.site.register(AnnualRevenue)
admin.site.register(Milestone)
admin.site.register(Project)
admin.site.register(Product)
admin.site.register(SuccessStories)
admin.site.register(Expertise, ExpertiseAdmin)
admin.site.register(Vertical, VerticalAdmin)
admin.site.register(Partnership)
admin.site.register(Alliance)
admin.site.register(TechnicalAssociation)