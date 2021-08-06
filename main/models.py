from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField

# Create your models here.


class Participant(models.Model):
	email = models.EmailField()

	def __str__(self):
		return f'{self.email}'

class Location(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.name} ({self.address})'

class Meetup(models.Model):
	title = models.CharField(max_length=200)
	organizer_email = models.EmailField()
	date = models.DateField()
	slug = models.SlugField(unique=True)
	description = models.TextField()
	image = models.ImageField(upload_to='images')
	location = models.ForeignKey(Location,on_delete=CASCADE)
	participant = models.ManyToManyField(Participant, blank=True, null=True)


	def __str__(self):
		return f'{self.title}'