try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url

from debug_toolbar.urls import _PREFIX

urlpatterns = patterns('debug_toolbar_user_panel.views',
    url(r'^%s/users/$' % _PREFIX, 'content',
        name='debug-userpanel'),
    url(r'^%s/users/login/$' % _PREFIX, 'login_form',
        name='debug-userpanel-login-form'),
    url(r'^%s/users/login/(?P<pk>-?\d+)$' % _PREFIX, 'login',
        name='debug-userpanel-login'),
    url(r'^%s/users/logout$' % _PREFIX, 'logout',
        name='debug-userpanel-logout'),
)
