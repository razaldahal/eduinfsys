from django.db import models
from django.utils import timezone
import datetime
from student.models import student


class Librarie(models.Model):
	Book=models.CharField(max_length=254)
	No_of_Books_Total=models.IntegerField()
	No_of_Books_Avilable=models.IntegerField()

	Of_Class=models.CharField(max_length=11)
	Of_Subject=models.CharField(max_length=20)
	Publisher_Name=models.CharField(max_length=64)
	Date_issued=models.DateField(default=datetime.date.today)
	Date_due=models.DateField(default=datetime.date.today)
	To=models.ForeignKey(student,on_delete=models.CASCADE)

	
	
	def __str__(self):
		return	self.Book 
