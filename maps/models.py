from django.db import models
from datetime import datetime


class Nokhetha(models.Model):
    nokhetha_name = models.CharField(max_length=200)
    nokhetha_desc = models.CharField(max_length=500)
    active_year_from = models.IntegerField()
    active_year_to = models.IntegerField()

    def __unicode__(self):
        return unicode(self.nokhetha_name)


class Location(models.Model):
    location_name = models.CharField(max_length=200)
    location_desc = models.CharField(max_length=500)
    latitude = models.DecimalField(max_digits=6, decimal_places=3)
    longitude = models.DecimalField(max_digits=6, decimal_places=3)

    def __unicode__(self):
        return unicode(self.location_name)


class TripEntry(models.Model):
    entry_locaiton = models.ForeignKey(Location, default=1)
    entry_desc = models.CharField(max_length=500)
    entry_date = models.DateField("Date", default=datetime.now, blank=True)
    entry_time = models.TimeField()
    zoom_level = models.IntegerField(default=8)

    def __unicode__(self):
        return unicode(self.entry_desc)


class Trip(models.Model):
    trip_name = models.CharField(max_length=200)
    trip_desc = models.CharField(max_length=500)
    nokhetha = models.ForeignKey(Nokhetha)
    trip_entries = models.ManyToManyField(to=TripEntry)

    def __unicode__(self):
        return unicode(self.trip_name)


