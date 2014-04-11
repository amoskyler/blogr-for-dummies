from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^(?P<user_name>.+)$', views.profile, name='profile')
)