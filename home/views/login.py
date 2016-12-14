from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from django.views import View
from django.contrib.auth import (
    authenticate,
    login
)
from django.http import HttpResponseRedirect

from home.forms.login import LoginForm


class LoginView(View):
    """ login view """
    template_name = 'home/login.html'

    def get(self, request, *args, **kwargs):
        """ get handler """
        context = self.get_context_data(
            request, 
            *args, 
            **kwargs
        )
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """ post handler """
        
        context = self.get_context_data(
            request,
            *args,
            **kwargs
        )
        form = context.get('form')

        if form and form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username', ''),
                password=form.cleaned_data.get('password', '')
            )

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, self.template_name, context)

