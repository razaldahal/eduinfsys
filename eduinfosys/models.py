from django.db import models
from django.utils import timezone

# Create your models here.
class classe(models.Model):
	Class=models.CharField(max_length=11)
	Section=models.CharField(max_length=2)
	Capacity=models.IntegerField()
	No_of_Students=models.IntegerField()
	def __str__(self):
 		return	self.Class
class section(models.Model):
	section=models.CharField(max_length=2)
	r_class=models.CharField(max_length=11)
	def __str__(self):
 		return	self.section

class teacher(models.Model):
	Classes=models.CharField(max_length=128)
	Subjects=models.CharField(max_length=128)
	Extras=models.CharField(max_length=120)
	Payments=models.CharField(max_length=120)
	Name=models.CharField(max_length=64)
	def __str__(self):
		return	self.Name
class student(models.Model):
	Class=models.CharField(max_length=11)
	Section=models.CharField(max_length=2)
	roll_no=models.IntegerField()
	Name=models.CharField(max_length=64)
	Father_name=models.CharField(max_length=64)
	Mother_name=models.CharField(max_length=64)
	Guardians_name=models.CharField(max_length=64)
	Guardians_contact=models.CharField(max_length=64)
	Address_Current=models.CharField(max_length=64)
	Address_Permanent=models.CharField(max_length=64)
	email=models.EmailField(max_length=64)
	def __str__(self):
 		return	self.Name 

class Librarie(models.Model):
	Book=models.CharField(max_length=254)
	No_of_Books_Total=models.IntegerField()
	No_of_Books_Avilable=models.IntegerField()
	Of_Class=models.CharField(max_length=11)
	Of_Subject=models.CharField(max_length=20)
	Publisher_Name=models.CharField(max_length=64)
	def __str__(self):
		return	self.Book 
class Parent(models.Model):
	Name_of_Father=models.CharField(max_length=64)
	Name_of_Mother=models.CharField(max_length=64)
	Contacts=models.CharField(max_length=20)
	Address_Permanent=models.CharField(max_length=64)
	Address_Current=models.CharField(max_length=64)
	Related_Student=models.ForeignKey(student,on_delete=models.CASCADE)
	def __str__(self):
		return	self.Name_of_Father+' - '+self.Name_of_Mother+' - '+self.Related_Student 
class Subject(models.Model):
	Name=models.CharField(max_length=64)
	Class=models.ForeignKey(classe,on_delete=models.CASCADE)
	Teacher=models.ForeignKey(teacher,on_delete=models.CASCADE)
	Book=models.CharField(max_length=64)
	def __str__(self):
		return	self.Name 	
class Exam(models.Model):
	Subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
	Class=models.ForeignKey(classe,on_delete=models.CASCADE)
	Date=models.DateTimeField()
	full_marks=models.IntegerField()
	pass_marks=models.IntegerField()
	def __str__(self):
		return	self.Subject+' - '+self.Date 
class Attendence(models.Model):
	
	student=models.ForeignKey(student,on_delete=models.CASCADE)
	Is_Present=models.BooleanField(default=True)
	Date=models.DateTimeField()
	def __str__(self):
		return	self.Date+' - '+self.student+' - ' +self.Is_Present

	
class Accounting(models.Model):
	student=models.ForeignKey(student,on_delete=models.CASCADE)
	fees_paid=models.IntegerField()
	fees_due=models.IntegerField()
	status=models.TextField()
	Date_of_Transaction=models.DateField()
	Time_of_Transaction=models.TimeField(default=timezone.now())
	
	def __str__(self):
		return self.student+' '+self.fees_paid+' '+self.fees_due









