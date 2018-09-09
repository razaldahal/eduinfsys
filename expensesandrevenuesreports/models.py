from django.db import models

# Create your models here.
class expensereports(models.Model):
	expense_type=
	expense_amount=
	date=
	approved_by=
	average_expense_week=
class expensespecailreport(models.Model):
	expense_category=
	expense_date_time=
	expense_object=
	quantity_of_object=
	expense_by=
	approved_by=
	ledger_record_name=
	ledger_page_no=
	expense_object_rate=
	expense_total_amount=
	description=
	reason_mentioned=
class revenuereport(models.Model):
	revenue_category=
	revenue_source=
	source_amount=
	average_revenue_month=
	date=
class revenuespecialreport(models.Model):
	revenue_type=
	revenue_amount=
	revenue_category=
	received_by=
	in_form=
	slip_or_cheque_no=
	date_time=
	received_from=
	receipt_no=
	ledger_name=
	ledger_page_no=
	receiver_contact=
	giver_contact=
	approved_transction_by=
	details=
	
