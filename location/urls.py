from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('location/', views.location_list),
    path('location/<int:pk>/', views.location_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)