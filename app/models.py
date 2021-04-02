from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class BOOKING(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	name = models.CharField(max_length=100)
	age = models.IntegerField(default=0)
	phone = PhoneNumberField(max_length=10)
	mode_of_transport = models.CharField(max_length=10,default= " " )
	price = models.IntegerField(default=0)
	total_cost = models.IntegerField(default=0)
	seat = models.IntegerField(default=0)
	source = models.CharField(max_length=100)
	destination = models.CharField(max_length=100)
	time = models.TimeField(auto_now=True)
	email = models.EmailField()



class FLIGHT(models.Model):
	source = models.CharField(max_length=100)
	destination = models.CharField(max_length=100)
	time = models.TimeField(auto_now=False)
	seat = models.IntegerField(default=15)
	price = models.IntegerField(default=0)

	@staticmethod
	def get_all_flights():
		return FLIGHT.objects.all()


class TRAIN(models.Model):
	source = models.CharField(max_length=100)
	destination = models.CharField(max_length=100)
	time = models.TimeField(auto_now=False)
	seat = models.IntegerField(default=15)
	price = models.IntegerField(default=0)

	@staticmethod
	def get_all_trains():
		return TRAIN.objects.all()

class BUS(models.Model):
	source = models.CharField(max_length=100)
	destination = models.CharField(max_length=100)
	time = models.TimeField(auto_now=False)
	seat = models.IntegerField(default=0)
	price = models.IntegerField(default=0)

	@staticmethod
	def get_all_buss():
		return BUS.objects.all()
