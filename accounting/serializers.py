from django.db import models

from rest_framework import serializers
from student.models import models
from .models import *



class AccountingSerializer(serializers.ModelSerializer):

	class Meta:
		model=Accounting
		fields=('student','fees_paid','fees_due','status','Date_of_Transaction','Time_of_Transaction')



