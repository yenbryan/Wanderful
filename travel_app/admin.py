from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from travel_app.models import Profile, Location, List,  Picture#, MushroomSpotHouse,
from django.contrib.gis import admin as gisadmin

admin.site.register(Profile)
admin.site.register(Location, gisadmin.OSMGeoAdmin)
admin.site.register(List)
admin.site.register(Picture)
#admin.site.register(House, gisadmin.OSMGeoAdmin)
#admin.site.register(MushroomSpot, LeafletGeoAdmin)


