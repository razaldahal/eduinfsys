from django.db import models
from django.contrib.auth.models import User,AbstractUser

	
	
class Role(models.Model):
  '''
  The Role entries are managed by the system,
  automatically created via a Django data migration.
  '''
  STUDENT = 1
  TEACHER = 2
  PRINCIPAL = 3
  HOD = 4
  INVENTORYSTAFF=5
  LIBRARIAN=6
  SECURITYSTAFF=7
  ACCOUNTANT=8
  HOSTELSTAFF=9
  BUSSTAFF=10
  OTHERSTAFF=11
  SHAREHOLDER=12
  PARENT=13
  ADMIN = 14
  CLASSTEACHER=15
  ROLE_CHOICES = (
      (STUDENT, 'student'),
      (TEACHER, 'teacher'),
      (PRINCIPAL, 'principal'),
      (HOD, 'HOD'),
      (INVENTORYSTAFF, 'inventorystaff'),
      (LIBRARIAN,'librarian'),
      (SECURITYSTAFF,'securitystaff'),
      (ACCOUNTANT,'accountant'),
      (HOSTELSTAFF,'hostelstaff'),
      (BUSSTAFF,'busstaff'),
      (OTHERSTAFF,'otherstaff'),
      (SHAREHOLDER,'shareholder'),
      (PARENT,'parent'),
      (ADMIN,'admin'),
      (CLASSTEACHER,'classteacher')
  )

  id = models.PositiveIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_id_display()


class User(AbstractUser):
  roles = models.ManyToManyField(Role)	
  choices=models.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=Role.ROLE_CHOICES)
  