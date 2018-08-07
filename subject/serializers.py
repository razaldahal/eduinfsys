from django.db import models

from rest_framework import serializers
from .models import *



class SubjectSerializer(serializers.ModelSerializer):

	class Meta:
		model=Subject
		fields=('Name',
			'Class',
			'Teacher',
			'Book')

