from django.db import models
from django.utils import timezone
import datetime




# Create your models here.
class classe(models.Model):
	Class=models.CharField(max_length=11)
	Capacity=models.IntegerField()
	No_of_Students=models.IntegerField()
	class Meta:
		unique_together=('Class',)
	
		
	def __str__(self):
		return self.Class