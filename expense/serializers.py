from rest_framework import serializers
from .models import *


class expenseSerializer(serializers.ModelSerializer):
	class Meta:
		model=Expense
		fields=('title','category','description','amount','method','date')


