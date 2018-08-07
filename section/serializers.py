from django.db import models

from rest_framework import serializers
from .models import *


class sectionSerializer(serializers.ModelSerializer):

	class Meta:
		model=section
		fields=('id','section','r_class')


