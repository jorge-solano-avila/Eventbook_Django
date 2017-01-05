from rest_framework.views import APIView
from rest_framework.response import Response
from models import City, Event


class Events( APIView ):
	def get( self, request, format = None ):
		return Response( { "events": {} } )

class EventsByType( APIView ):
	def get( self, request, format = None ):
		return Response( { "events": {} } )

class EventsByDistance( APIView ):
	def get( self, request, format = None ):
		return Response( { "events": {} } )

class EventsByDate( APIView ):
	def get( self, request, format = None ):
		return Response( { "events": {} } )