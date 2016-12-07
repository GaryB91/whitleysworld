from django.views.generic.list import ListView

from story.models import Story


class StoryListView(ListView):
    """ stories list """
    model = Story
    template_name = 'story/stories.html'

