# pylint: disable=invalid-name
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ddesk/', include('ddesk.urls')),
    path('admin/', admin.site.urls)
]
