from django.urls import path
from . import views


#Create url patterns


urlpatterns = [
	
	path('', views.index, name='meetups'),
	path("<slug:slug>/success/", views.confirm_registration, name='cornfirm-registration'),
	path("<slug:slug>/", views.meetup_details, name="meetup-detail"),

]