# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class student(models.Model):
	select_gender=(
	('G','Select One'), 
	('M', 'Male'),
	('F','Female'),
	('O', 'Other'),
	)

	select_gender=models.CharField(max_length=2,choices=select_gender)
	full_name=models.CharField(max_length=64)
	address=models.CharField(max_length=128)
	grade=models.CharField(max_length=11)
	section=models.CharField(max_length=3)
	roll_no=models.IntegerField()

class grade(models.Model):
	select_grade=(
	('N','Nursery'),
	('L', 'L.KG.'),
	('U','U.KG.'),
	('1', 'One'),
	('2', 'Two'),
	('3','Three'),
	('4', 'Four'),
	('5', 'Five'),
	('6', 'Six'),
	('7', 'Seven'),
	('8', 'Eight'),
	('9', 'Nine'),
	('x','Ten'),
	('xi', 'Eleven'),
	('xii','Twelve')
	
	)
	
	select_grade=models.CharField(max_length=3, choices=select_grade)
	select_section=(
			('A','A'),
			('B','B'),
			('C', 'C'),
			('D', 'D'),
			('E', 'E'),
			('F', 'F'),
			('G', 'G'),
			('H', 'H'),
			('I', 'I'),
 			('J', 'J'),
			('K','K'),
			)
	select_section=models.CharField(max_length=1,choices=select_section)
class teacher(models.Model):
	full_name=models.CharField(max_length=64)
	address=models.CharField(max_length=128)
	phone_no=models.CharField(max_length=16)
	qualifications=models.CharField(max_length=60)
	

