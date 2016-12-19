from django.contrib import admin
from story.models import Story
from story.models import Page
# Register your models here.

class StoryAdmin(admin.ModelAdmin):
	"""story admin"""
	pass
admin.site.register(Story, StoryAdmin)


class PageAdmin(admin.ModelAdmin):
	"""page admin"""
	pass
admin.site.register(Page, PageAdmin)

