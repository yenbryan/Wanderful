from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):

    def __unicode__(self):
        return self.username


class Location(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name


class List(models.Model):
    profile = models.ForeignKey(Profile, related_name="lists")
    location = models.ManyToManyField(Location, related_name="lists")
    list_name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.list_name


class Picture(models.Model):
    image = models.ImageField(upload_to='travel_images', blank=True, null=True)
    description = models.CharField(max_length=140)
    location = models.ForeignKey(Location, related_name="pictures")

