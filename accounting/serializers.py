from django.db import models

from rest_framework import serializers
from student.models import models
from .models import *



class accountingSerializer(serializers.ModelSerializer):

	class Meta:
		model=accounting
		fields=('student','fees_paid','status','Date_of_Transaction','Time_of_Transaction')



