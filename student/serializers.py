from django.db import models

from rest_framework import serializers
from .models import *


class studentSerializer(serializers.ModelSerializer):

	class Meta:
		model=student
		fields=('Class',
				'Section',
				'roll_no',
				'Name',
				'Father_name',
				'Mother_name',
				'Guardians_name',
				'Guardians_contact',
				'Address_Current',
				'Address_Permanent',)


