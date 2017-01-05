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
			return Response( { "error": 2, "description": "User with email = " + email + " doesn't exist" } )

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

			return Response( { "user": userAux } )
		else:
			return Response( { "error": 3, "description": "Invalid password" } )