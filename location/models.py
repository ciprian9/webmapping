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
class Location(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, default='')
    lat = models.TextField()
    long = models.TextField()

    class Meta:
        ordering = ('created',)

class WorldBorder(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()   
    pop2005 = models.IntegerField('Population 2005')    
    fips = models.CharField('FIPS Code', max_length=2)    
    iso2 = models.CharField('2 Digit ISO', max_length=2)    
    iso3 = models.CharField('3 Digit iso', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-region code')
    lon = models.FloatField()
    lat = models.FloatField()


    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
 """

class UserProfile(models.Model):
     uid = models.CharField(max_length=100, blank=True, verbose_name='uid', primary_key=True)
     uname = models.EmailField(verbose_name='email')
     last_location = models.PointField(verbose_name="last_location", blank=True)
     created = models.DateTimeField(auto_now_add=True)
     modified = models.DateTimeField(auto_now=True)


class DublinBikes(models.Model):
    stand_number = models.IntegerField(verbose_name='number',blank=False,primary_key=True)
    stand_name = models.CharField(max_length=80,verbose_name="name",blank=False)
    total_bike_stands = models.IntegerField(default=0,verbose_name="bike_stands",blank=False)
    available_bike_stands = models.IntegerField(default=0,verbose_name="available_bike_stands",blank=False)
    available_bikes = models.IntegerField(default=0,verbose_name="available_bikes",blank=False)
    last_update = models.DateTimeField(default=timezone.now())
    position =models.PointField(verbose_name='position')
    


