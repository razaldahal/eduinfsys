'''from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from student.models import student
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status'''

'''class AccountingViewsets(viewsets.ModelViewSet):
	queryset=Accounting.objects.all()
	serializer_class=AccountingSerializer


	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			Accounting.objects.get_or_create(student=data['student'],defaults={'Date_of_Transaction':data['Date_of_Transaction'],'Time_of_Transaction':data['Time_of_Transaction'],'fees_paid':data['fees_paid'],'fees_due':data['fees_due'],'status':data['status']})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		sec = Accounting.objects.get(id=pk)
		serializer = self.get_serializer(data=sec)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.student,obj.Date_of_Transaction,obj.fees_due,obj.status})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.student = data['student']
			obj.Date_of_Transaction=data['Date_of_Transaction']
			obj.fees_paid=data['fees_paid']
			obj.fees_due=data['fees_due']
			obj.status=data['status']
			obj.Time_of_Transaction=data['Time_of_Transaction']
			

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			Accounting.objects.get(pk=pk).delete()	
			return Response(status.HTTP_204_NO_CONTENT)
'''






from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework import serializers
from .models import *
from .serializers import *
from rest_framework import request
from rest_framework.response import Response
from rest_framework import generics







class accountingList(generics.ListCreateAPIView):
	queryset = accounting.objects.all()
	serializer_class = accountingSerializer


class accountingDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = accounting.objects.all()
	serializer_class = accountingSerializer

