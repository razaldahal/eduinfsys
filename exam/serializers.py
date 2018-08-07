from django.db import models

from rest_framework import serializers

from .models import *
			
class ExamSerializer(serializers.ModelSerializer):

	class Meta:
		model=Exam
		fields=('Subject',
				'Class',
				'Date',
				'full_marks',
				'pass_marks')

