from django.db import models
from django.utils import timezone
import datetime



class section(models.Model):
	section=models.CharField(max_length=2)
	r_class=models.CharField(max_length=11)
	def __str__(self):
 		return	self.section
