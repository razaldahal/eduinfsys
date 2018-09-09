from django.db import models

from rest_framework import serializers
from .models import *


class timetableSerializer(serializers.ModelSerializer):

	class Meta:
		model=timetable
		fields=('Class','Section','Event','Event_description','Teacher','Subject','Time_start','Time_end','Day','Date')


