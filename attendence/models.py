from django.db import models
from django.utils import timezone
import datetime
from student.models import student
from teacher.models import teacher

class attendence(models.Model):
	teacher=models.ForeignKey(teacher,on_delete=models.CASCADE)
	student=models.ForeignKey(student,on_delete=models.CASCADE)
	Is_Present=models.BooleanField(default=True)
	Date=models.DateTimeField()
	def __str__(self):
		return	self.Date+' - '+self.student+' - ' +self.Is_Present
