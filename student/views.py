'''from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework import status


class studentViewsets(viewsets.ModelViewSet):
	queryset=student.objects.all()
	serializer_class=studentSerializer

	

	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			student.objects.get_or_create(Name=data['Name'],defaults={'Class':data['Class'],'Section':data['Section'],'roll_no':data['roll_no'],'Father_name':data['Father_name'],'Mother_name':data['Mother_name'],'Guardians_name':data['Guardians_name'],'Guardians_contact':data['Guardians_contact'],'Address_current':data['Address_current'],'Address_permanent':data['Address_permanent'],'email':data['email']})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		std = student.objects.get(id=pk)
		serializer = self.get_serializer(data=std)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.Name,obj.Class,obj.Section,obj.roll_no})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.Name = data['Name']
			obj.Class=data['Class']
			obj.Section=data['Section']
			obj.roll_no=data['roll_no']
			obj.Father_name=data['Father_name']
			obj.Mother_name=data['Mother_name']
			obj.Guardians_name=data['Guardians_name']
			obj.Guardians_contact=data['Guardians_contact']
			obj.Address_current=data['Address_current']
			obj.Address_permanent=data['Address_permanent']
			obj.email=data['email']

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			student.objects.get(pk=pk).delete()	

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




class studentList(generics.ListCreateAPIView):
	queryset = student.objects.all()
	serializer_class = studentSerializer

class studentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = student.objects.all()
	serializer_class = studentSerializer
	
	
	
class qualificationList(generics.ListCreateAPIView):
	queryset = qualifications.objects.all()
	serializer_class = qualificationSerializer


class qualificationDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = qualifications.objects.all()
	serializer_class = qualificationSerializer

class admissionList(generics.ListCreateAPIView):
	queryset = admission.objects.all()
	serializer_class = admissionSerializer


class admissionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = admission.objects.all()
	serializer_class = admissionSerializer
	

class otherList(generics.ListCreateAPIView):
	queryset = other.objects.all()
	serializer_class = otherSerializer


class otherDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = other.objects.all()
	serializer_class = otherSerializer


class hostelList(generics.ListCreateAPIView):
	queryset = hostel.objects.all()
	serializer_class = hostelSerializer


class hostelDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = hostel.objects.all()
	serializer_class = hostelSerializer