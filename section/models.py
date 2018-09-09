from django.db import models
from django.utils import timezone
import datetime
from classe.models import *






class section(models.Model):
	r_class=models.ForeignKey(classe,on_delete=models.CASCADE)
	section=models.CharField(max_length=2)
	class Meta:
		unique_together=('r_class','section')
	
	def __str__(self):
 		return self.section+'-'+self.r_class.Class
