from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from api.views import router

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'app.views.index'),
    (r'^dashboard/$', 'app.views.dashboard'),
    (r'^settings/$', 'app.views.settings'),
    (r'^inbound/$', 'app.views.inbound'),

    (r'^accounts/', include('userena.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^api/me/$', 'api.views.me'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    (r'', include('social_auth.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
