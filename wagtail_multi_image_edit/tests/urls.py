from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include, url

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_multi_image_editurls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail_multi_image_edit.views import multi_image_edit


private_urlpatterns = [
    url(r'^admin/images/multi-edit/', multi_image_edit, name='multi_image_edit'),
    path('django-admin/', admin.site.urls),
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
]

urlpatterns = [
]

urlpatterns = private_urlpatterns + urlpatterns + [
    # Add Wagtail URLs at the end.
    # Wagtail cache-control is set on the page models's serve methods.
]
