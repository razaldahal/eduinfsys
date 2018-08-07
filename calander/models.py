from django.db import models
from django.utils import timezone
import datetime




class Calander(models.Model):
	Date=models.DateField()
	Event=models.CharField(max_length=64)
	Details=models.TextField()





