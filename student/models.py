from django.db import models
from django.utils import timezone
import datetime

from section.models import *
from django_countries.fields import CountryField 





class student(models.Model):
	Section_Class=models.ForeignKey(section,on_delete=models.CASCADE)
	roll_no=models.IntegerField()
	Name=models.CharField(max_length=64)
	Father_name=models.CharField(max_length=64)
	Mother_name=models.CharField(max_length=64)
	Guardians_name=models.CharField(max_length=64)
	Guardians_contact=models.CharField(max_length=64)
	country=CountryField()
	Address_current=models.CharField(max_length=64)
	Address_permanent=models.CharField(max_length=64)
	email=models.EmailField(max_length=64)
	mobile=models.CharField(max_length=20)
	class Meta:
		unique_together=('Section_Class','roll_no')
	def __str__(self):
 		return str(self.id)+' '+self.Name
 		
class qualifications(models.Model):
	previous_institution=models.CharField(max_length=100)
	address_of_the_institution=models.TextField()
	qualifications=models.CharField(max_length=100)
	def __str__(self):
		return self.qualifications
	
class admission(models.Model):
	student=models.ForeignKey('student',on_delete=models.CASCADE)
	qualifications=models.ForeignKey('qualifications',on_delete=models.CASCADE)
	join_date=models.DateField()
	batch=models.CharField(max_length=64)
	course=models.CharField(max_length=64)
	academic_year=models.CharField(max_length=64,default='2018'+'-'+'2019')
	
	
class other(models.Model):
	admission_fee=models.IntegerField()
	
class hostel(models.Model):
	hostel=models.BooleanField()			
	hostel_name=models.CharField(max_length=100)
	hostel_address=models.CharField(max_length=200)
	hostel_room=models.CharField(max_length=20)
	reg_date=models.DateField()
	vacation_date=models.DateField()	
