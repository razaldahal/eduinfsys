from django.db import models

from rest_framework import serializers
from student.models import student
from .models import *


class LibrarieSerializer(serializers.ModelSerializer):

	class Meta:
		model=Librarie
		fields=('Book',
				'No_of_Books_Total',
				'No_of_Books_Avilable',
				'Of_Class',
				'Of_Subject',
				'Publisher_Name',
				'Date_issued',
				'Date_due',
				'To'
				
				)



