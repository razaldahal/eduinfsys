'''from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework import status

class SubjectViewsets(viewsets.ModelViewSet):
	queryset=Subject.objects.all()
	serializer_class=SubjectSerializer


	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			Subject.objects.get_or_create(Name=data['Name'],defaults={'Class':data['Class'],'Teacher':data['Teacher'],'Book':data['Book']})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		sub = Subject.objects.get(id=pk)
		serializer = self.get_serializer(data=sub)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.Name,obj.Class,obj.Book})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.Name = data['Name']
			obj.Class=data['Class']
			obj.Teacher=data['Teacher']
			obj.Book=data['Book']

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			Subject.objects.get(pk=pk).delete()	

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







class subjectList(generics.ListCreateAPIView):
	queryset = subject.objects.all()
	serializer_class = subjectSerializer


class subjectDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = subject.objects.all()
	serializer_class = subjectSerializer

