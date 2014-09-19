from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.gis.db import models as gismodels
from django.utils.text import slugify
from djgeojson.fields import PointField

class Profile(AbstractUser):

    def __unicode__(self):
        return self.username


class Location(models.Model):
    name = models.CharField(max_length=60)
    geom = gismodels.PointField(null=True)
    address = models.CharField(max_length=150)
    #list = models.ForeignKey(List, related_name='locations')

    @property
    def popupContent(self):
        return '<p><{}</p>'.format(self.address)
        #return '<img src="{}" /><p><{}</p>'.format(self.picture.url, self.address)

    def __unicode__(self):
        return self.name


class List(models.Model):
    profile = models.ForeignKey(Profile,
                                related_name="lists")
    location = models.ManyToManyField(Location,
                                      related_name="lists",
                                      null=True,
                                      blank=True)
    list_name = models.CharField(max_length=60)
    slug_name = models.SlugField()


    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.list_name)
        super(List, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.list_name


class Picture(models.Model):
    image = models.ImageField(upload_to='travel_images',
                              blank=True,
                              null=True)
    description = models.CharField(max_length=140)
    location = models.ForeignKey(Location,
                                 related_name="pictures")

# class House(models.Model):
#     geom = gismodels.PointField()

# class MushroomSpot(models.Model):
#
#     geom = PointField()
#     # description = models.TextField()
#     # picture = models.ImageField()

    # @property
    # def popupContent(self):
    #   return '<img src="{}" /><p><{}</p>'.format(
    #       self.picture.url,
    #       sel f.description)
