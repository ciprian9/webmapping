"""
from rest_framework import serializers
from .models import Location, WorldBorder

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'title', 'lat', 'long')


    def create(self, validated_data):
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.long = validated_data.get('long', instance.long)
        instance.save()
        return instance



class WorldBorderSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    area = serializers.IntegerField()
    pop2005 = serializers.IntegerField()
    fips = serializers.CharField(required=False, max_length=2)
    iso2 = serializers.CharField(required=False, max_length=2)
    iso3 = serializers.CharField(required=False, max_length=3)
    un = serializers.IntegerField()
    region = serializers.IntegerField()
    subregion = serializers.IntegerField()
    lon = serializers.FloatField()
    lat = serializers.FloatField()

    def create(self, validated_data):
        return WorldBorder.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.area = validated_data.get('area', instance.area)
        instance.pop2005 = validated_data('pop2005', instance.pop2005)
        instance.fips = validated_data.get('fips', instance.fips)
        instance.iso2 = validated_data.get('iso2', instance.iso2)
        instance.iso3 = validated_data.get('iso3', instance.iso3)
        instance.un = validated_data.get('un', instance.un)
        instance.region = validated_data.get('region', instance.region)
        instance.subregion = validated_data.get('subregion', instance.subregion)
        instance.lon = validated_data.get('lon', instance.lon)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.save()
        return instance

        """
