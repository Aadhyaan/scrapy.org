from django.conf import settings
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('django.views.generic.simple',
    url(r"^$", 'direct_to_template', {'template': 'pages/home.html'}),
    url(r"^download/", 'direct_to_template', {'template': 'pages/download.html'}),
    url(r"^doc/", 'direct_to_template', {'template': 'pages/doc.html'}),
    url(r"^community/", 'direct_to_template', {'template': 'pages/community.html'}),
    # for ie6 png hack
    url(r"^blank.gif$", 'redirect_to', {'url': '%s/style/blank.gif' % settings.MEDIA_URL})
)

if settings.DEBUG: # devel
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL[1:], \
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
