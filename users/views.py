from rest_framework.views import APIView
from rest_framework.response import Response
from models import User


class UserInformation( APIView ):
	def post( self, request, format = None ):
		email = request.data["email"]
		password = request.data["password"]
		try:
			user = User.objects.get( email = email )
		except User.DoesNotExist:
			return Response( { "error": 2, "description": "User with email = " + email + " doesn't exist", "success": False } )

		if user.password == password:
			events = [{
				"name": event.name, 
				"type": event.type,
				"startDateTime": event.startDateTime,
				"finishDateTime": event.finishDateTime,
				"latitude": event.latitude,
				"longitude": event.longitude
			} for event in user.events.all()]
			userAux = {
				"name": user.name,
				"lastName": user.lastName,
				"email": user.email,
				"events": events
			}

			return Response( { "user": userAux, "success": True } )
		else:
			return Response( { "error": 3, "description": "Invalid password", "success": False } )

class AddUser( APIView ):
	def post( self, request, format = None ):
		name = request.data["name"]
		lastName = request.data["lastName"]
		email = request.data["email"]
		password = request.data["password"]
		
		userExist = User.objects.filter( email = email ).exists()
		if userExist:
			return Response( { "error": 4, "description": "User with email = " + email + " exist" } )

		User.objects.create( name = name, lastName = lastName, email = email, password = password )
		return Response( { "success": True } )