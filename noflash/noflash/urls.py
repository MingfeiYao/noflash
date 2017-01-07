from django.conf.urls import url
from django.contrib import admin
from homepage.views import homepage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', homepage),
]
