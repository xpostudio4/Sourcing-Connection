from fileupload.models import Picture
from django.contrib import admin

class PictureAdmin(admin.ModelAdmin):
    pass

admin.site.register(Picture, PictureAdmin)
