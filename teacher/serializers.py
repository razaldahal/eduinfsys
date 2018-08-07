from django.db import models

from rest_framework import serializers
from .models import *





class teacherSerializer(serializers.ModelSerializer):

	class Meta:
		model=teacher
		fields=('Classes','Subjects','Extras','Payments','Name')

	
