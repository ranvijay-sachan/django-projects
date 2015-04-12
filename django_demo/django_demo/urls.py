from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_demo.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^articles/', include('article.urls')),


    # user auth urls
    url(r'^$', 'django_demo.views.login'),
    url(r'^accounts/auth/$', 'django_demo.views.auth_view'),
    url(r'^accounts/logout/$', 'django_demo.views.logout'),
    url(r'^accounts/loggedin/$', 'django_demo.views.loggedin'),
    url(r'^accounts/invalid/$', 'django_demo.views.invalid_login'),

    url(r'^accounts/register/$', 'django_demo.views.register_user'),
    url(r'^accounts/register_success/$', 'django_demo.views.register_success'),

)
