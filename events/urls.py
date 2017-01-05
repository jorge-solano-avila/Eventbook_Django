from django.conf.urls import url
from events import views

urlpatterns = [
	url( r"^events$", views.Events.as_view() ),
	url( r"^events-type$", views.EventsByType.as_view() ),
	url( r"^events-distance$", views.EventsByDistance.as_view() ),
	url( r"^events-date$", views.EventsByDate.as_view() )
]