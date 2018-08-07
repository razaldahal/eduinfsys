from django.db import models
from django.utils import timezone
import datetime
from classe.models import classe
from section.models import section
from teacher.models import teacher
from subject.models import Subject




class timetable(models.Model):
	Class=models.ForeignKey(classe,on_delete=models.CASCADE)
	Section=models.ForeignKey(section,on_delete=models.CASCADE)
	Teacher=models.ForeignKey(teacher,on_delete=models.CASCADE)
	Subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
	Time_start=models.TimeField()
	Time_end=models.TimeField()
	Day=(
		('0','Sunday'),
		('1','Monday'),
		('2','Tuesday'),
		('3','Wednesday'),
		('4','Thursday'),
		('5','Friday'),
		('6','Saturday'),
		)


	Day=models.CharField(max_length=1,choices=Day)
	Date=models.DateField()
	def __str__(self):
		return self.Teacher+' '+self.Day+' '+self.Class+self.Section+' '+self.Time_start
