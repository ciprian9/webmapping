from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.gis import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('location/', views.location_list),
    path('location/<int:pk>/', views.location_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
