from django.conf.urls import url

from story.views.stories import StoryListView
from story.views.page import PageView


app_name = 'story'
urlpatterns = [
    url(r'^$', StoryListView.as_view(), name='stories'),
    url(r'(?P<story>[\w-]+)/(?P<page>\w+)/', PageView.as_view(), name='page')
]

