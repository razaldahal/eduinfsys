from django.db import models

from rest_framework import serializers
from .models import *

class calanderSerializer(serializers.ModelSerializer):

	class Meta:
		model=calander
		fields=('Date','Event','Details')



