from django.db import models
from django.utils import timezone
import datetime



class noticeboard(models.Model):
	Name=models.CharField(max_length=64)
	Date_Published=models.DateField()
	Details=models.TextField()
	Date_Expiry=models.DateField()
	
	def __str__(self):
		return self.Name+' '+self.Date_Published+' '+self.Date_Expiry
