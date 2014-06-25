from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
     url(r'^$', 'codex.views.home'),
)

urlpatterns += staticfiles_urlpatterns()
