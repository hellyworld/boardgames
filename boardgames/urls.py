from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('user.urls')),
    url(r'^$', 'main.views.home', name='boardgames_home'),
)

# url mappings named boardgames_login or boardgames_logout
urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^login/$', 'login',  # this is django.contrib.auth.views.login
        {'template_name': 'login.html'},
        name='boardgames_login'),

    url(r'^logout/$', 'logout',  # this is django.contrib.auth.views.logout
        {'next_page': 'boardgames_home'},
        name='boardgames_logout'),
)
