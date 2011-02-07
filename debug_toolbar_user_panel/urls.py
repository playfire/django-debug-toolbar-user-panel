from django.conf.urls.defaults import patterns, url

from debug_toolbar.urls import _PREFIX

urlpatterns = patterns('debug_toolbar_user_panel.views',
    url(r'^%s/users/$' % _PREFIX, 'content',
        name='debug-userpanel'),
    url(r'^%s/users/(?P<pk>\d+)/$' % _PREFIX, 'login',
        name='debug-userpanel-login'),
)
