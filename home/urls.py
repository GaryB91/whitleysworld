from django.conf.urls import url

from home.views.home import HomeView, AboutView
from home.views.login import LoginView
from home.views.logout import LogoutView
from home.views.register import RegisterView


app_name = 'home'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout')
]

