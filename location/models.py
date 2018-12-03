from django.db import models
from django.contrib.gis.db import models

# Create your models here.


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
