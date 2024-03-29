"""
api URL Configuration
"""

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    # API
    url(r'^v1/', include('v1.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
