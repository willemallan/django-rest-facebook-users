from django.conf.urls import patterns, url

urlpatterns = patterns('clients.views',
    url(r'^$', 'client_list'),
    url(r'^(?P<facebook_id>[0-9]+)/$', 'client_detail'),
)