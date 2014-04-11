from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.login, name='login'),
	url(r'^register$', views.register, name='register'),
	url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^(?P<user_name>.+)$', views.profile, name='profile'),
)
