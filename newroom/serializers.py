from django.db import models

from rest_framework import serializers
from .models import *




class newroomSerializer(serializers.ModelSerializer):

	class Meta:
		model=newroom
		fields=('Class','Section','Name','Awards','Description')



