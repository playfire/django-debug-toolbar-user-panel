import debug_toolbar.urls

try:
    from django.conf.urls import patterns, include
except ImportError:
    from django.conf.urls.defaults import patterns, include

from .urls import urlpatterns

debug_toolbar.urls.urlpatterns += patterns('',
    ('', include(urlpatterns)),
)
