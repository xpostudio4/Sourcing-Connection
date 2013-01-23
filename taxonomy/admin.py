from taxonomy.models import Industry, Technology as Tech, Category, Application as App
from taxonomy.models import Tag
from django.contrib import admin

class IndustryAdmin(admin.ModelAdmin):
    pass

class TechAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

class AppAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Industry, IndustryAdmin)
admin.site.register(Tech, TechAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(App, AppAdmin)
admin.site.register(Tag, TagAdmin)
