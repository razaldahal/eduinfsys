from django.db import models
from django.utils import timezone
import datetime
from subject.models import Subject
from classe.models import classe


class Exam(models.Model):
	Subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
	Class=models.ForeignKey(classe,on_delete=models.CASCADE)
	Date=models.DateTimeField()
	full_marks=models.IntegerField()
	pass_marks=models.IntegerField()
	def __str__(self):
		return	self.Subject+' - '+self.Date 
