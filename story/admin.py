from django.contrib import admin
from story.models import Story
from story.models import Page
# Register your models here.

class StoryAdmin(admin.ModelAdmin):
	"""story admin"""
	prepopulated_fields = {"slug": ("title",)} 
admin.site.register(Story, StoryAdmin)


class PageAdmin(admin.ModelAdmin):
	"""page admin"""
	raw_id_fields = ["story"]
admin.site.register(Page, PageAdmin)

