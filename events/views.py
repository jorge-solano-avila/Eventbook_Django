from rest_framework.views import APIView
from rest_framework.response import Response
from models import City, Event
import json
import requests


class Events( APIView ):
	def get( self, request, format = None ):
		latitude = request.query_params["latitude"]
		longitude = request.query_params["longitude"]

		latLng = latitude + "," + longitude
		response = requests.get( "http://maps.googleapis.com/maps/api/geocode/json?latlng=" + latLng )
		if response.status_code == 200:
			response = response.json()
			placeId = response["results"][4]["place_id"]

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
			"longitude": event.longitude,
			"cityId": city.id
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