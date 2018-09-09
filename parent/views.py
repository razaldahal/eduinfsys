'''from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

class ParentViewsets(viewsets.ModelViewSet):
	queryset=Parent.objects.all()
	serializer_class=ParentSerializer


	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			Parent.objects.get_or_create(Name_of_Father=data['Name_of_Father'],Name_of_Mother=data['Name_of_Mother'],Related_Student=data['Related_Student'],defaults={'Contacts':data['Contacts'],'Address_current':data['Address_current'],'Address_permanent':data['Address_permanent']})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		Par = Par.objects.get(id=pk)
		serializer = self.get_serializer(data=Par)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.Name_of_Father,obj.Name_of_Mother,obj.Related_Student})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.Name_of_Father = data['Name_of_Father']
			obj.Name_of_Mother=data['Name_of_Mother']
			obj.Related_Student=data['Related_Student']
			obj.Address_current=data['Address_current']
			obj.Address_permanent=data['Address_permanent']
			obj.Contacts=data['Contacts']

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			Parent.objects.get(pk=pk).delete()	

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







class parentList(generics.ListCreateAPIView):
	queryset = parent.objects.all()
	serializer_class = parentSerializer


class parentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = parent.objects.all()
	serializer_class = parentSerializer

