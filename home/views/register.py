from django.views.generic.edit import FormView

from home.forms.register import RegistrationForm


class RegisterView(FormView):
    """ registration view """
    
    template_name = 'home/register.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        """ form valid override """
        form.save()
        return super(RegisterView, self).form_valid(form)

