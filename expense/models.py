from django.db import models

# Create your models here.
class Expense(models.Model):
	title=models.CharField(max_length=64)
	category=models.CharField(max_length=64)
	description=models.TextField()
	amount=models.IntegerField()
	method=(
		('0','Cash'),
		('1','Cheque'),
		)
	method=models.CharField(max_length=20,choices=method)
	date=models.DateField() 
