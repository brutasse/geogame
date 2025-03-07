from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse

admin.autodiscover()

from questions import views

urlpatterns = patterns('',
    url(r'^$', views.question, name='question'),
    url(r'^leaderboard/$', views.user_stats, name='leaderboard'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth/', include('users.urls')),

     url(r'^robots.txt$', lambda _:
         HttpResponse('User-agent: *\nDisallow:\n', mimetype='text/plain')),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
