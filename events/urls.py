from django.conf.urls import url
from events import views

urlpatterns = [
	url( r"^events$", views.Events.as_view() )
]