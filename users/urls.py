from django.conf.urls import url
from users import views

urlpatterns = [
	url( r"^user$", views.User.as_view() )
]