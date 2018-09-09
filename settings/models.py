from django.db import models
from django_countries.fields import CountryField


from django.utils import timezone
# Create your models here.
class Institution(models.Model):
    name=models.CharField(max_length=255)
    address=models.TextField()
    email=models.EmailField()
    phone_no=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)
    fax=models.CharField(max_length=20)
    admin_contact_person=models.CharField(max_length=64)
    country=models.CharField(max_length=2)
    currency=models.CharField(max_length=10)
    Institution_code=models.CharField(max_length=5)
    def __str__(self):
    	return str(self.id)+"--"+self.address+"--"+self.name+','
    
class Academics(models.Model):
    start_year=models.CharField(max_length=12)
    start_month=models.CharField(max_length=20)
    end_year=models.CharField(max_length=12)
    end_month=models.CharField(max_length=20)
    Active_Deactive=(
                    ('A','Active'),
                    ('D','Deactive'),
                    )
    Active_Deactive=models.CharField(max_length=1,choices=Active_Deactive)

class Caste_Religion(models.Model):
    student_caste=models.CharField(max_length=30)
    student_religion=models.CharField(max_length=30)       
