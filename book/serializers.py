from rest_framework import serializers
from .models import *

class bookSerializer(serializers.ModelSerializer):

	class Meta:
		model=book
		fields=('serial_no','name','author','publisher','edition')
		