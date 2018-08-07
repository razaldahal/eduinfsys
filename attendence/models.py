from django.db import models
from django.utils import timezone
import datetime
from student.models import student

class Attendence(models.Model):
	
	student=models.ForeignKey(student,on_delete=models.CASCADE)
	Is_Present=models.BooleanField(default=True)
	Date=models.DateTimeField()
	def __str__(self):
		return	self.Date+' - '+self.student+' - ' +self.Is_Present
