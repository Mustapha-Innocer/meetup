from main.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Location, Meetup

# Create your views here.


def index(request):
	meetups = Meetup.objects.all()
	if len(meetups) == 0:
		return render(request, 'main/index.html',{
			'meetup_empty': True,
			'meetups':meetups
		})
	else:
		return render(request, 'main/index.html',{
			'meetup_empty': False,
			'meetups':meetups
		})

def meetup_details(request, slug):
	try:
		selected_meetup = Meetup.objects.get(slug = slug)
		if request.method == "GET":
			registration_form = RegistrationForm()
			
		else:
			registration_form = RegistrationForm(request.POST)
			if registration_form.is_valid():
				participant = registration_form.save()
				selected_meetup.participant.add(participant)
				return redirect('cornfirm-registration', slug=slug )

		return render(request, 'main/meetup-detail.html',{
				'meetup_empty':False,	
				'meetup':selected_meetup,
				'form': registration_form,
			})

	except Exception as e:
		print(e)
		return render(request, 'main/meetup-detail.html',{
			'meetup_empty':True,	
		})

def confirm_registration(request,slug):
	return render(request, 'main/registration-success.html')