from django.db import models
from django.utils import timezone
import datetime
from classe.models import classe
from section.models import section





class newroom(models.Model):
	Class=models.ForeignKey(classe,on_delete=models.CASCADE)
	Section=models.ForeignKey(section,on_delete=models.CASCADE)
	Name=models.CharField(max_length=64)
	Awards=models.CharField(max_length=128)
	Description=models.TextField()
