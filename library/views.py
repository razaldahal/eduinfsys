from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from student.models import student
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class LibrarieViewsets(viewsets.ModelViewSet):
	queryset=Librarie.objects.all()
	serializer_class=LibrarieSerializer

	

	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			Librarie.objects.get_or_create(Book=data['Book'],defaults={'No_of_Books_Total':data['No_of_Books_Total'],'No_of_Books_Avilable':data['No_of_Books_Avilable'],'Of_Class':data['Of_Class'],'Of_Subject':data['Of_Subject'],'Publisher_Name':data['Publisher_Name'],'Date_issued':data['Date_issued'],'Date_due':data['Date_due'],'To':data['To']})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		lib = Librarie.objects.get(id=pk)
		serializer = self.get_serializer(data=lib)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.Name,obj.Subjects,obj.Classes})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.Book = data['Book']
			obj.No_of_Books_Total=data['No_of_Books_Total']
			obj.No_of_Books_Avilable=data['No_of_Books_Avilable']
			obj.Of_Class=data['Of_Class']
			obj.Of_Subject=data['Of_Subject']
			obj.Publisher_Name=data['Publisher_Name']
			obj.Date_issued=data['Date_issued']
			obj.Date_due=data['Date_due']
			obj.To=data['To']

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			Librarie.objects.get(pk=pk).delete()	

			return Response(status.HTTP_204_NO_CONTENT)

