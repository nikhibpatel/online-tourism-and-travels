from django.db import models

# Create your models here.

class BOOKING(models.Model):
	passenger_name = models.CharField(max_length=100)
	passenger_age  = models.IntegerField(default = 2)
	passenger_mobile_no = models.IntegerField(default = 2)
	mode_of_transport = models.CharField(max_length=100,default= " " )
	date_of_arrival = models.DateTimeField('date published')

