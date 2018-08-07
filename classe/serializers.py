from django.db import models

from rest_framework import serializers
from .models import *

class classeSerializer(serializers.ModelSerializer):

	class Meta:
		model=classe
		fields=('Class','Section','Capacity','No_of_Students')



