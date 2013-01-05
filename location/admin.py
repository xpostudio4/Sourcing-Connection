from location.models import Country, Region, City
from django.contrib import admin


class CountryAdmin(admin.ModelAdmin):
    pass
class RegionAdmin(admin.ModelAdmin):
    pass
class CityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
