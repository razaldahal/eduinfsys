from django.db import models

# Create your models here.\
class principal(models.Model):
	name=
	address=
	citizenship_no=
	email=
	phone_no=
	photo=
	principal_from_date=
	short_description=
	is_shareholder=
	current_share_percentage
class share_holders(models.Model):
	name=
	address=
	occupation=
	citizenship_no=
	eamil=
	phone_no=
	joined_date=
	intial_share_amount=
	cuurent_share_percentage=
	monthly_income_share=
	photo=
	short_description=
	intro_by=
	approved_by=
class HODs(models.Model):
	name=
	address=
	phone_no=
	department_or_level=
	appointed_date=
	own_subject=
	departmental_performance_remarks=
	salary=
	bonuses_and_awards=
	appointed_by=
	appointed_method=
	approved_by=
	reports_to=
class Class_teachers(models.Model):
	name=
	address=
	phone_no=
	eamil=
	subject=
	of_class_section=
	appointed_date=
	appointed_by=
	appointed_method=
	approved_by=
	salary_monthly=
	performance_remarks=
	reports_to=
	photo=
		
class Hostel_staffs(models.Model):
	staff_type=
	name=
	address=
	phone_no=
	work_start_date=
	salary=
	timetable=
	performace_remarks=
	reports_to=
	appointed_by=
	approved_by=
	work_days=
	
	
	























	