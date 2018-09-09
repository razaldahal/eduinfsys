from django.db import models

# Create your models here.
class libraryreports(models.Model):
	librarian=
	total_no_of_books=
	average_price=
	books_required_no=
	total_cost_required=
	book=
	
class librarymembeshipreports(models.Model):
	total_members=
	total_new_members_month=
	total_old_members=
	total_retired_members_month=
	total_terminated_members_month=
	average_revenue_from_membership_month=
class inventoryreports(models.Model):
	item_type=
	manufacturer=
	quantity=
	cost_per_item=
	product_name=
class inventorymoneyreports(models.Model):
	item_type_required=
	quantity_required=
	cost_per_item=
	manufacturer=
	name=
	total_item_expense=
	date_time_of_transactions=
	items_sold_month=
	total_revenue_month=
	total_expense_month=
class accountingreports(models.Model):
	transaction_type=
	date_time=
	accountant=
	total_income_from_type=
	total_expense_from_type=
	general_description=
	remarks=
class accountingspecialreport(models.Model):
	transaction_type=
	transaction_date_time=
	accountant=
	object_of_transaction=
	related_account=
	related_person=
	related_persons_contact_no=
	reason_of_transaction=
	income_or_expense=
	amount=
	related_receipt_or_slip_no=
	related cheque_no_or_cash=
	registered_ledger_no=
	amount_effected_on_main_account=
	verifeid_by=
	details=
	proof_of_verifiction=
	contact_of_person_verified=

class 	
	
	
	
	
	
	
	