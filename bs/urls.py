from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^api/', include('bs_app.urls')),
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
