from django.db import models
from django.utils import timezone
import datetime



# Create your models here.
class classe(models.Model):
	Class=models.CharField(max_length=11)
	Section=models.CharField(max_length=2)
	Capacity=models.IntegerField()
	No_of_Students=models.IntegerField()
	def __str__(self):
 		return	self.Class
