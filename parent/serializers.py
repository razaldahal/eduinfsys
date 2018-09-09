from django.db import models

from rest_framework import serializers
from .models import *




class parentSerializer(serializers.ModelSerializer):

	class Meta:
		model=parent
		fields=('Name_of_Father',
				'occupation_of_father',
				'Name_of_Mother',
				'occupation_of_mother',
				'Contact_No_Father',
				'Contact_No_Mother',
				'Address_Permanent',
				'Address_Current',
				'Related_Student')

