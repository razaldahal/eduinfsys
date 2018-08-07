from django.db import models
from django.utils import timezone
import datetime
from student.models import student



class teacher(models.Model):
	Classes=models.CharField(max_length=128)
	Subjects=models.CharField(max_length=128)
	Extras=models.CharField(max_length=120)
	Payments=models.CharField(max_length=120)
	Name=models.CharField(max_length=64)
	def __str__(self):
		return	self.Name
