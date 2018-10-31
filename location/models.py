from django.db import models

# Create your models here.


class Location(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, default='')
    lat = models.TextField()
    long = models.TextField()

    class Meta:
        ordering = ('created',)

