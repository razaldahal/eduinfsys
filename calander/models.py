from django.db import models
from django.utils import timezone
import datetime




class calander(models.Model):
	Date=models.DateField()
	Event=models.CharField(max_length=64)
	Details=models.TextField()





