from django.db import models
from django.utils import timezone
import datetime
from student.models import student


class Accounting(models.Model):
	student=models.ForeignKey(student,on_delete=models.CASCADE)
	fees_paid=models.IntegerField()
	fees_due=models.IntegerField()
	status=models.TextField()
	Date_of_Transaction=models.DateField()
	Time_of_Transaction=models.TimeField(default=timezone.now())


	
	def __str__(self):
		return self.student+' '+self.fees_paid+' '+self.fees_due
