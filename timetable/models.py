from django.db import models
from django.utils import timezone
import datetime
from classe.models import classe
from section.models import section
from teacher.models import teacher
from subject.models import subject




class timetable(models.Model):
	user=
	Time_start=models.TimeField()
	Time_end=models.TimeField()
	Event=models.CharField(max_length=80)
	Event_description=models.TextField()
	
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
