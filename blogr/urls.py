from django.conf.urls import patterns, include, url

from django.contrib import admin
from blog import views
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.login, name='login'),
	url(r'^newuser/$', views.new_user, name='new_user'),
 	url(r'^blog/', include('blog.urls')),
 	url(r'^admin/', include(admin.site.urls)),
)