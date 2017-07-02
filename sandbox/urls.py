import wagtail.wagtailadmin.urls
from django.conf.urls import include, url
from django.contrib import admin
from wagtail.wagtailcore import urls as wagtail_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cms/', include(wagtail.wagtailadmin.urls)),
    url(r'', include(wagtail_urls)),
]
