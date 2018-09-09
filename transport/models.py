from django.db import models

# Create your models here.
class transport(models.Model):
	vehicle_number=models.CharField(max_length=20)
	route=models.CharField(max_length=30)
	time_departure=models.TimeField()
	time_return=models.TimeField()
