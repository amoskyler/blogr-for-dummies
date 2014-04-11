from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views
admin.autodiscover()

urlpatterns = patterns('',
<<<<<<< HEAD
	url(r'^$', views.login, name='login'),
	url(r'^register$', views.register, name='register'),
	url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^(?P<user_name>.+)$', views.profile, name='profile'),
)
=======
	url(r'^$', views.login, namespace='login'),
	url(r'^newuser/$', views.new_user, namespace='new_user'),
 	url(r'^blog/', include('blog.urls'), namespace = 'blog'),
 	url(r'^admin/', include(admin.site.urls), namespace = 'admin'),
)
>>>>>>> 24454ca01677045fc10cf15f7315adf2660f9ffb
