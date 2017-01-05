from __future__ import unicode_literals
from django.db import models


class City( models.Model ):
	name = name = models.CharField( db_column = "Name", max_length = 255, null = False, blank = False )

	def __unicode__( self ):
        return self.name

class Event( models.Model ):
	TYPE_CHOICES = (
		( "CO", "Concert" ),
		( "SP", "Sport" ),
		( "CI", "Cinema" ),
		( "TH", "Theater" ),
		( "PR", "Programming" ),
		( "OT", "Other" ),
	)

	name = models.CharField( db_column = "Name", max_length = 255, null = False, blank = False )
	type = models.CharField( db_column = "Type", max_length = 2, choices = TYPE_CHOICES, default = "OT" )
	description = models.TextField( db_column = "Description", null = True, blank = True )
	city = models.ForeignKey( City )
	startDateTime = models.DateTimeField( db_column = "StartDateTime", null = False, blank = False )
	finishDateTime = models.DateTimeField( db_column = "FinishDateTime", null = False, blank = False )

	def __unicode__( self ):
        return str( self.id ) + " - " + self.name