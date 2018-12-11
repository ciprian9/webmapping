import datetime

from django.utils import timezone

from django.db import models
from django.contrib.gis.db import models as models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.contrib.gis.geos import Point
# Create your models here.


"""
    model for the dublin bikes table used to hold all the data for each bike stand
"""
class DublinBikes(models.Model):
    stand_number = models.IntegerField(verbose_name='number',blank=False,primary_key=True)
    stand_name = models.CharField(max_length=80,verbose_name="name",blank=False)
    total_bike_stands = models.IntegerField(default=0,verbose_name="bike_stands",blank=False)
    available_bike_stands = models.IntegerField(default=0,verbose_name="available_bike_stands",blank=False)
    available_bikes = models.IntegerField(default=0,verbose_name="available_bikes",blank=False)
    last_update = models.DateTimeField(default=timezone.now())
    position =models.PointField(verbose_name='position')
    

