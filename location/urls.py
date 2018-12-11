from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.gis import admin


urlpatterns = [
]

urlpatterns = format_suffix_patterns(urlpatterns)
