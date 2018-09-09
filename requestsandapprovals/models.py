from django.db import models

# Create your models here.
class requests(models.Model):
	request_type=
	requested_by=
	request_details=
	request_reasons=
	request_cost_amount=
	request_completion_days=
	approve_request=
class approvals(models.Model):	
	approval_type=
	date_approved=
	aprroved_by=
	approved_requests
	pending_approvals_requests=
	unapproved_requests=

