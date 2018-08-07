from django.db import models

from rest_framework import serializers
from student.models import student	
from .models import *


	
class AttendenceSerializer(serializers.ModelSerializer):

	class Meta:
			model=Attendence
			fields=('Date',
				'student',
				'Is_Present')





