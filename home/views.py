from django.views.generic.base import TemplateView

# Create your views here

class HomeView(TemplateView):
    """ Home page view """

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        """ context data """
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

