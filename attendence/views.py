from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers

from student.models import student
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status



class AttendenceViewsets(viewsets.ModelViewSet):
	queryset=Attendence.objects.all()
	serializer_class=AttendenceSerializer

	

	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			Attendence.objects.get_or_create(student=data['student'],defaults={'Is_Present':data['Is_Present'],'Date':data['Date']})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		att = Attendence.objects.get(id=pk)
		serializer = self.get_serializer(data=att)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.student,obj.Date,obj.Is_Present})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.student = data['student']
			obj.Date=data['Date']
			obj.Is_Present=data['Is_Present']
			

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			Attendence.objects.get(pk=pk).delete()	

			return Response(status.HTTP_204_NO_CONTENT)
