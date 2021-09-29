# pylint: disable=invalid-name
from django.contrib import admin
from django.urls import path

from ddesk.views import index

urlpatterns = [
    path('ddesk/', index),
    path('admin/', admin.site.urls)
]
