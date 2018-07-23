from django.conf.urls import patterns,url,include

urlpatterns = patterns('user.views',
    url(r'^home$', 'home', name='user_home')
)
