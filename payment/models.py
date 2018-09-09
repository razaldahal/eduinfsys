from django.db import models
from student.models import *

class Invoice(models.Model):
	student=models.ForeignKey(student,on_delete=models.CASCADE)
	title=models.CharField(max_length=64)
	description=models.TextField()
	total=models.IntegerField()
	status=(
		('0','Paid'),
		('1','Due'),
		)
	status=models.CharField(max_length=1,choices=status)
	method=(
		('0','Cash'),
		('1','Cheque'),
		)
	method=models.CharField(max_length=20,choices=method)
	date=models.DateField()

	def __str__(self):
		return self.student+' '+self.status

