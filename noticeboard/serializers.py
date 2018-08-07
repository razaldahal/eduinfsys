from django.db import models

from rest_framework import serializers
from .models import *


class noticeboardSerializer(serializers.ModelSerializer):

	class Meta:
		model=noticeboard
		fields=('Name','Date_Published','Details','Date_Expiry')




