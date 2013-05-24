from recommendations.models import *
from django.contrib import admin

class RecommendationAdmin(admin.ModelAdmin):
	pass

admin.site.register(Recommendation, RecommendationAdmin)
