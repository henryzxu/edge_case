from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.expand_profile, name='expand_profile'),
    url(r'^submit_profile/$', views.submit_profile, name='submit_profile'),
    url(r'^submit/$', views.submit, name='submit'),
]
