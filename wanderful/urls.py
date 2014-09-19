from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from djgeojson.views import GeoJSONLayerView
from travel_app.forms import LoginForm, ResetPWord
#from travel_app.models import MushroomSpot

from wanderful import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wanderful.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'travel_app.views.home', name='home'),
    url(r'^profile/$', 'travel_app.views.profile', name='profile'),

    url(r'^register/$', 'travel_app.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', kwargs={'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', kwargs={'next_page': '/'}, name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', kwargs={'password_reset_form': ResetPWord}, name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    #registration shit
    url(r'register/$', 'travel_app.views.register', name='register'),

    url(r'list-it/$', 'travel_app.views.list_it', name='list_it'),
    url(r'view-list/(?P<list_slug>[\w-]+)/$', 'travel_app.views.view_list', name='view_list'),
    url(r'edit-list/(?P<list_slug>[\w-]+)/edit$', 'travel_app.views.edit_list', name='edit_list'),

    url(r'location/$', 'travel_app.views.location', name='location'),

    url(r'view-location/(?P<location_id>\d+)/$', 'travel_app.views.view_location', name='view_location'),
    url(r'edit-location/(?P<location_id>\d+)/edit$', 'travel_app.views.edit_location', name='edit_location'),

    url(r'upload/picture/(?P<location_id>\d+)/$', 'travel_app.views.upload_picture', name="upload_picture"),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)