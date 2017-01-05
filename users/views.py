from rest_framework.views import APIView
from rest_framework.response import Response
from models import User


class UserInformation( APIView ):
	def get( self, request, format=None ):
		return Response( { "user": {} } )