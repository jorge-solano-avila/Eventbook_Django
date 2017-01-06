from rest_framework.views import APIView
from rest_framework.response import Response
from models import City, Event


class Events( APIView ):
	def get( self, request, format = None ):
		placeId = request.query_params["placeId"]
		try:
			city = City.objects.get( placeId = placeId )
		except City.DoesNotExist:
			return Response( { "error": 1, "description": "City with place id = " + str( placeId ) + " doesn't exist", "success": False } )
		
		events = Event.objects.filter( city = city )
		eventsAux = [
		{
			"name": event.name,
			"type": event.type,
			"startDateTime": event.startDateTime,
			"finishDateTime": event.finishDateTime,
			"latitude": event.latitude,
			"longitude": event.longitude
		} for event in events]

		return Response( { "events": eventsAux, "success": True } )

class EventsByType( APIView ):
	def get( self, request, format = None ):
		placeId = request.query_params["placeId"]
		try:
			city = City.objects.get( placeId = placeId )
		except City.DoesNotExist:
			return Response( { "error": 1, "description": "City with place id = " + str( placeId ) + " doesn't exist", "success": False } )
		
		events = Event.objects.filter( city = city, type = request.query_params["type"] )
		eventsAux = [
		{
			"name": event.name, 
			"type": event.type,
			"startDateTime": event.startDateTime,
			"finishDateTime": event.finishDateTime,
			"latitude": event.latitude,
			"longitude": event.longitude
		} for event in events]

		return Response( { "events": eventsAux, "success": True } )

class EventsByDistance( APIView ):
	def get( self, request, format = None ):
		placeId = request.query_params["placeId"]
		try:
			city = City.objects.get( placeId = placeId )
		except City.DoesNotExist:
			return Response( { "error": 1, "description": "City with place id = " + str( placeId ) + " doesn't exist", "success": False } )
		
		events = Event.objects.filter( city = city )
		eventsAux = [
		{
			"name": event.name, 
			"type": event.type,
			"startDateTime": event.startDateTime,
			"finishDateTime": event.finishDateTime,
			"latitude": event.latitude,
			"longitude": event.longitude
		} for event in events]

		return Response( { "events": eventsAux, "success": True } )

class EventsByDate( APIView ):
	def get( self, request, format = None ):
		placeId = request.query_params["placeId"]
		try:
			city = City.objects.get( placeId = placeId )
		except City.DoesNotExist:
			return Response( { "error": 1, "description": "City with place id = " + str( placeId ) + " doesn't exist", "success": False } )
		
		events = Event.objects.filter( city = city )
		eventsAux = [
		{
			"name": event.name, 
			"type": event.type,
			"startDateTime": event.startDateTime,
			"finishDateTime": event.finishDateTime,
			"latitude": event.latitude,
			"longitude": event.longitude
		} for event in events]

		return Response( { "events": eventsAux, "success": True } )