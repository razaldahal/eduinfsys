from django.db import models

from rest_framework import serializers
from .models import *
from django_countries.serializers import CountryFieldMixin


class studentSerializer(CountryFieldMixin,serializers.ModelSerializer):

	class Meta:
		model=student
		fields=('id',
				'Section_Class',
				'roll_no',
				'Name',
				'Father_name',
				'Mother_name',
				'Guardians_name',
				'Guardians_contact',
				'Address_current',
				'Address_permanent',
				'country',
					'email',
					'mobile')
					
class qualificationSerializer(serializers.ModelSerializer):

	class Meta:
		model=qualifications
		fields=('previous_institution','address_of_the_institution','qualifications')
	
class admissionSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=admission
		fields=('student','qualifications','batch','academic_year','join_date','course')
class otherSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=other
		fields=('admission_fee',)
class hostelSerializer(serializers.ModelSerializer):
	class Meta:
		model=hostel
		fields=('hostel','hostel_name','hostel_address','hostel_room','reg_date','vacation_date')				
