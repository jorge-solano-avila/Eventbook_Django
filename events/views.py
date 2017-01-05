from rest_framework.views import APIView
from rest_framework.response import Response
from models import City, Event


class Events( APIView ):
	def get( self, request, format = None ):
		cityId = request.query_params["id"]
		try:
			City.objects.get( id = cityId )
		except City.DoesNotExist:
			return Response( { "error": 1, "description": "City with id = " + str( cityId ) + " doesn't exist" } )
		
		events = Event.objects.filter( city__id = cityId )
		eventsAux = [
		{
			"name": event.name, 
			"type": event.type,
			"startDateTime": event.startDateTime,
			"finishDateTime": event.finishDateTime,
			"latitude": event.latitude,
			"longitude": event.longitude
		} for event in events]

		return Response( { "events": eventsAux } )

class EventsByType( APIView ):
	def get( self, request, format = None ):
		cityId = request.query_params["id"]
		try:
			City.objects.get( id = cityId )
		except City.DoesNotExist:
			return Response( { "error": 1, "description": "City with id = " + str( cityId ) + " doesn't exist" } )
		
		events = Event.objects.filter( city__id = cityId, type = request.query_params["type"] )
		eventsAux = [
		{
			"name": event.name, 
			"type": event.type,
			"startDateTime": event.startDateTime,
			"finishDateTime": event.finishDateTime,
			"latitude": event.latitude,
			"longitude": event.longitude
		} for event in events]

		return Response( { "events": eventsAux } )

class EventsByDistance( APIView ):
	def get( self, request, format = None ):
		cityId = request.query_params["id"]
		try:
			City.objects.get( id = cityId )
		except City.DoesNotExist:
			return Response( { "error": 1, "description": "City with id = " + str( cityId ) + " doesn't exist" } )
		
		events = Event.objects.filter( city__id = cityId )
		eventsAux = [
		{
			"name": event.name, 
			"type": event.type,
			"startDateTime": event.startDateTime,
			"finishDateTime": event.finishDateTime,
			"latitude": event.latitude,
			"longitude": event.longitude
		} for event in events]

		return Response( { "events": eventsAux } )

class EventsByDate( APIView ):
	def get( self, request, format = None ):
		cityId = request.query_params["id"]
		try:
			City.objects.get( id = cityId )
		except City.DoesNotExist:
			return Response( { "error": 1, "description": "City with id = " + str( cityId ) + " doesn't exist" } )
		
		events = Event.objects.filter( city__id = cityId )
		eventsAux = [
		{
			"name": event.name, 
			"type": event.type,
			"startDateTime": event.startDateTime,
			"finishDateTime": event.finishDateTime,
			"latitude": event.latitude,
			"longitude": event.longitude
		} for event in events]

		return Response( { "events": eventsAux } )