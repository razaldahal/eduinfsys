'''from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

class timetableViewsets(viewsets.ModelViewSet):
	queryset=timetable.objects.all()
	serializer_class=timetableSerializer

	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			timetable.objects.get_or_create(Time_start=data['Time_start'],Time_end=data['Time_end'],Teacher=data['Teacher'],defaults={'Class':data['Class'],'Section':data['Section'],'Subject':data['Subject'],'Day':data['Day'],Date:data['Date']})
		return Response(data)	
	def get(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			self.get_object(pk=pk)
		return Response(data)	
	def retrieve(self,request,pk,format=None):
		obj=self.get_object(pk=pk)
		return Response({obj.Class,obj.Section,obj.Teacher,obj.Day,obj.Time_start,obj.Time_end})
	def update(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		data={}
		if serializer.is_valid():
			data=serializer.data
			obj=self.get_object()
			obj.Class=data['Class']
			obj.Section=data['Section']
			obj.Subject=data['Subject']
			obj.Teacher=data['Teacher']
			obj.Day=data['Day']
			obj.Time_start=data['Time_start']
			obj.Time_end=data['Time_end']
			obj.Date=data['Date']
			obj.save()
	def delete(self,request,pk):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			timetable.objects.get(pk=pk).delete()
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







class timetableList(generics.ListCreateAPIView):
	queryset = timetable.objects.all()
	serializer_class = timetableSerializer


class timetableDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = timetable.objects.all()
	serializer_class = timetableSerializer

