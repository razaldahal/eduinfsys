'''from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

class noticeboardViewsets(viewsets.ModelViewSet):
	queryset=noticeboard.objects.all()
	serializer_class=noticeboardSerializer

	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			noticeboard.objects.get_or_create(Name=data['Name'],Date_Published=data['Date_Published'],defaults={'Details':data['Details'],Date_Expiry:data['Date_Expiry']})
			return Response(data)
		else:
			return Response(serializer.errors)	

	def get(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		notice=noticeboard.objects.get(pk=pk)		
		return Response(notice.data)
	def retrive(self,request,pk,format=None):
		obj=self.get_object(pk=pk)

		return Response({obj.data})
	def update(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		data={}
		if serializer.is_valid():
			data=serializer.data
			obj=self.get_object(pk=pk)
			data=serializer.data
			obj.Name=data['Name']
			obj.Date_Published=data['Date_Published']
			obj.Details=data['Details']
			obj.Date_Expiry=data['Date_Expiry']
			obj.save()
		return Response(data)
	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
	
		if serializer.is_valid():
			data=serializer.data
			noticeboard.objects.get(pk=pk).delete()
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







class noticeboardList(generics.ListCreateAPIView):
	queryset = noticeboard.objects.all()
	serializer_class = noticeboardSerializer


class noticeboardDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = noticeboard.objects.all()
	serializer_class = noticeboardSerializer

