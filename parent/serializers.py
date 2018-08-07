from django.db import models

from rest_framework import serializers
from .models import *




class ParentSerializer(serializers.ModelSerializer):

	class Meta:
		model=Parent
		fields=('Name_of_Father',
				'Name_of_Mother',
				'Contacts',
				'Address_Permanent',
				'Address_Current',
				'Related_Student')

