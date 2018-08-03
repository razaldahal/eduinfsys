from django.db import models

from rest_framework import serializers
from eduinfosys.models import *

class classeSerializer(serializers.ModelSerializer):

	class Meta:
		model=classe
		fields=('Class','Section','Capacity','No_of_Students')
class sectionSerializer(serializers.ModelSerializer):

	class Meta:
		model=section
		fields=('id','section','r_class')


class teacherSerializer(serializers.ModelSerializer):

	class Meta:
		model=teacher
		fields=('Classes','Subjects','Extras','Payments','Name')
class studentSerializer(serializers.ModelSerializer):

	class Meta:
		model=student
		fields=('Class',
				'Section',
				'roll_no',
				'Name',
				'Father_name',
				'Mother_name',
				'Guardians_name',
				'Guardians_contact',
				'Address_Current',
				'Address_Permanent',
				'email')
class LibrarieSerializer(serializers.ModelSerializer):

	class Meta:
		model=Librarie
		fields=('Book',
				'No_of_Books_Total',
				'No_of_Books_Avilable',
				'Of_Class',
				'Of_Subject',
				'Publisher_Name')


class ParentSerializer(serializers.ModelSerializer):

	class Meta:
		model=Parent
		fields=('Name_of_Father',
				'Name_of_Mother',
				'Contacts',
				'Address_Permanent',
				'Address_Current',
				'Related_Student')
class SubjectSerializer(serializers.ModelSerializer):

	class Meta:
		model=Subject
		fields=('Name',
			'Class',
			'Teacher',
			'Book')
class ExamSerializer(serializers.ModelSerializer):

	class Meta:
		model=Exam
		fields=('Subject',
				'Class',
				'Date',
				'full_marks',
				'pass_marks')
class AttendenceSerializer(serializers.ModelSerializer):

	class Meta:
			model=Attendence
			fields=('Date',
				'student',
				'Is_Present')

class AccountingSerializer(serializers.ModelSerializer):

	class Meta:
		model=Accounting
		fields=('student','fees_paid','fees_due','status','Date_of_Transaction','Time_of_Transaction')