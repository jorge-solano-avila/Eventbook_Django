from django.conf.urls import url
from users import views

urlpatterns = [
	url( r"^user$", views.UserInformation.as_view() ),
	url( r"^add-user$", views.AddUser.as_view() )
]