from django.contrib import admin
from users.models import User


class UserAdmin( admin.ModelAdmin ):
	search_fields = ["id", "name", "lastName", "email"]
	list_display = ( "id", "name", "lastName", "email" )

admin.site.register( User, UserAdmin )