from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from subject.models import Subject
from classe.models import classe
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ExamViewsets(viewsets.ModelViewSet):
	queryset=Exam.objects.all()
	serializer_class=ExamSerializer



	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			Exam.objects.get_or_create(Subject=data['Subject'],defaults={'Class':data['Class'],'Date':data['Date'],'full_marks':data['full_marks'],'pass_marks':data['pass_marks']})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		Exm = Exam.objects.get(id=pk)
		serializer = self.get_serializer(data=Exm)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.Subject,obj.Class,obj.Date})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.Subject = data['Subject']
			obj.Class=data['Class']
			obj.Date=data['Date']
			obj.full_marks=data['full_marks']

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			Subject.objects.get(pk=pk).delete()	

			return Response(status.HTTP_204_NO_CONTENT)
