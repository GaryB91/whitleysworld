from django.views.generic.base import TemplateView

# Create your views here

class HomeView(TemplateView):
    """ Home page view """

    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        """ context data """
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

class AboutView(TemplateView):
    """ About page view """

    template_name = "home/about.html"

    def get_context_data(self, **kwargs):
        """ context data """
        context = super(AboutView, self).get_context_data(**kwargs)
        return context

