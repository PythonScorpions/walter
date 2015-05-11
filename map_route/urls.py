from django.conf.urls import patterns, include, url
from userapp import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index_view.as_view(), name="login_user"),
    url(r'^maps$', views.map_view.as_view(), name="maps"),
    # url(r'^map_route/', include('map_route.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
 url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
