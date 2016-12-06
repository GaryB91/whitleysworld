from django.contrib.auth import logout
from django.views import View
from django.http import HttpResponseRedirect


class LogoutView(View):
    """ logout view """

    def get(self, request, *args, **kwargs):
        """ get handler """
        if request.user.is_authenticated:
            logout(request)
        return HttpResponseRedirect('/')

