from django.db import models

class busrecords(models.Model):
	number_plate=
	driver=
	route=
	type_or_size=
	timetable=
	no_of_passengers=
	average_revenue=
class busexpenses(models.Model):
	number_plate=
	route=
	fuel_expenses=
	repair_expenses=
	age=
	damage_expenses=
class specialevents(models.Model):
	event_name=
	event_description=
	consequence=
	date_time=
	driver=
	route=
		