from django.contrib import admin
from news.models import Post 

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('name',)}
	list_display = ('name', 'created', 'user')

admin.site.register(Post, PostAdmin)