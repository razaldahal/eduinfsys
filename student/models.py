from django.db import models
from django.utils import timezone
import datetime





class student(models.Model):
	Class=models.CharField(max_length=11)
	Section=models.CharField(max_length=2)
	roll_no=models.IntegerField()
	Name=models.CharField(max_length=64)
	Father_name=models.CharField(max_length=64)
	Mother_name=models.CharField(max_length=64)
	Guardians_name=models.CharField(max_length=64)
	Guardians_contact=models.CharField(max_length=64)
	Address_Current=models.CharField(max_length=64)
	Address_Permanent=models.CharField(max_length=64)
	email=models.EmailField(max_length=64)
	def __str__(self):
 		return	self.Name 
