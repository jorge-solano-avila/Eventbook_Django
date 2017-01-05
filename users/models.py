from __future__ import unicode_literals
from django.db import models
from events.models import Event


class User( models.Model ):
	name = models.CharField( db_column = "Name", max_length = 255, null = False, blank = False )
	lastName = models.CharField( db_column = "LastName", max_length = 255, null = False, blank = False )
	email = models.EmailField( db_column = "Email", max_length = 255, null = False, blank = False )
	password = models.CharField( db_column = "Password", max_length = 255, null = False, blank = False )
	events = models.ManyToManyField( Event, blank = True )