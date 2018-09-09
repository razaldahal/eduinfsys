from django.db import models

from rest_framework import serializers
from .models import *



class subjectSerializer(serializers.ModelSerializer):

	class Meta:
		model=subject
		fields=('Name',
			'Class',
			'Teacher',
			'Book')

