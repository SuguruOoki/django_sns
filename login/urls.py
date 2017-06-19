from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^in/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^out/$', 'django.contrib.auth.views.logout',
        {'template_name': 'logged_out.html'}),
]
