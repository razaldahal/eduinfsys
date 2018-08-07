from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status


class sectionViewsets(viewsets.ModelViewSet):
	queryset=section.objects.all()
	serializer_class=sectionSerializer

	http_methods = ['post', 'put', 'get', 'delete']

	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get_or_create(section=data['section'],defaults={'r_class':data['r_class'],})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		sec = section.objects.get(id=pk)
		serializer = self.get_serializer(data=sec)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.section,obj.r_class})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.section = data['section']
			obj.r_class=data['r_class']

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			section.objects.get(pk=pk).delete()	

			return Response(status.HTTP_204_NO_CONTENT)


