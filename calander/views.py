from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers

from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class CalanderViewsets(viewsets.ModelViewSet):
	queryset=Calander.objects.all()
	serializer_class=CalanderSerializer

	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			Calander.objects.get_or_create(Date=data['Date'],Event=data['Event'],Details=data['Details'])
			return Response(data)
		else:
			return(serializer.errors)
	def get(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			Calander.objects.get(pk=pk)
			return Response(data)
	def retrive(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			obj=Calander.objects.get(pk=pk)
			return Response({obj.data})
	def update(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		data={}
		if serializer.is_valid():
			data=serializer.data
			obj=self.get_object(pk=pk)
			obj.Date=data['Date']
			obj.Event=data['Event']
			obj.Details=data['Details']
			obj.save()
		return Response(data)
	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			Calander.objects.get(pk=pk).delete()									
							
