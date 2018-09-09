from django.db import models
from django.utils import timezone
import datetime
from student.models import student


class parent(models.Model):
	Name_of_Father=models.CharField(max_length=64)
	occupation_of_father=models.CharField(max_length=64)
	Name_of_Mother=models.CharField(max_length=64)
	occupation_of_mother=models.CharField(max_length=64)
	Contact_No_Father=models.CharField(max_length=20)
	Contact_No_Mother=models.CharField(max_length=20)
	Address_Permanent=models.CharField(max_length=64)
	Address_Current=models.CharField(max_length=64)
	Related_Student=models.ForeignKey(student,on_delete=models.CASCADE)
	def __str__(self):
		return	self.Name_of_Father+' - '+self.Name_of_Mother+' - '+self.Related_Student 
