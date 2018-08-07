from django.db import models

from rest_framework import serializers
from .models import *

class CalanderSerializer(serializers.ModelSerializer):

	class Meta:
		model=Calander
		fields=('Date','Event','Details')



