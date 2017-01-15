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
			return Response( { "error": 2, "description": "User with email = " + email + " doesn't exist", "translation": "ERROR.USER_DOES_NOT_EXIST", "success": False } )

		if user.password == password:
			events = [{
				"id": event.id,
				"name": event.name, 
				"type": event.type,
				"description": event.description,
				"startDateTime": event.startDateTime,
				"finishDateTime": event.finishDateTime,
				"latitude": event.latitude,
				"longitude": event.longitude,
				"cityId": event.city.id
			} for event in user.events.all()]
			userAux = {
				"id": user.id,
				"name": user.name,
				"lastName": user.lastName,
				"email": user.email,
				"events": events
			}

			return Response( { "user": userAux, "success": True } )
		else:
			return Response( { "error": 3, "description": "Invalid password", "translation": "ERROR.PASSWORD_INCORRECT", "success": False } )

class AddUser( APIView ):
	def post( self, request, format = None ):
		name = request.data["name"]
		lastName = request.data["lastName"]
		email = request.data["email"]
		password = request.data["password"]
		
		userExist = User.objects.filter( email = email ).exists()
		if userExist:
			return Response( { "error": 4, "description": "User with email = " + email + " exist", "translation": "ERROR.USER_EXISTS", "success": False } )

		user = User.objects.create( name = name, lastName = lastName, email = email, password = password )
		userAux = {
			"id": user.id,
			"name": user.name,
			"lastName": user.lastName,
			"email": user.email,
			"events": []
		}

		return Response( { "user": userAux, "success": True } )