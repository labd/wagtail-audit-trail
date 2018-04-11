import wagtail.admin.urls
from django.conf.urls import include, url
from django.contrib import admin
from wagtail.core import urls as wagtail_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cms/', include(wagtail.admin.urls)),
    url(r'', include(wagtail_urls)),
]
