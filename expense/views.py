from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework import serializers
from .models import *
from .serializers import *
from rest_framework import request
from rest_framework.response import Response
from rest_framework import generics

class ExpenseList(generics.ListCreateAPIView):
	queryset = Expense.objects.all()
	serializer_class = expenseSerializer
	
class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Expense.objects.all()
	serializer_class = expenseSerializer
