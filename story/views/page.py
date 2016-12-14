from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render

from story.models import Page


class PageView(View):
    """ page view """

    template_name = 'story/page.html'

    def get(self, request, *args, **kwargs):
        """ get handler """
        page_number = kwargs.get('page')
        story = kwargs.get('story')

        try:
            page = Page.objects.select_related(
                'story'
            ).get(
                story__slug=story,
                number=page_number
            )
        except Page.DoesNotExist:
            return HttpResponseRedirect('/stories/')
        
        context = {
            'page': page,
            'story': page.story,
            'has_next': page_number < page.story.pages.count(),
            'has_previous': page_number > 1
        }
        return render(request, self.template_name, context)

