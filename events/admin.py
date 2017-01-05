from django.contrib import admin
from events.models import City, Event


class CityAdmin( admin.ModelAdmin ):
	search_fields = ["id", "placeId", "name"]
	list_display = ( "id", "placeId", "name" )

class EventAdmin( admin.ModelAdmin ):
	search_fields = ["id", "name", "type", "latitude", "longitude"]
	raw_id_fields = ["city"]
	list_display = ( "id", "name", "type", "description", "city", "startDateTime", "finishDateTime", "latitude", "longitude" )

admin.site.register( City, CityAdmin )
admin.site.register( Event, EventAdmin )