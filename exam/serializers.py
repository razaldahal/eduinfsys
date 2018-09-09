from django.db import models

from rest_framework import serializers

from .models import *
			
class examSerializer(serializers.ModelSerializer):

	class Meta:
		model=exam
		fields=('Subject',
				'Class',
				'Date_time',
				'full_marks',
				'pass_marks')

