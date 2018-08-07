from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from classe.models import classe
from section.models import section
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class newroomViewsets(viewsets.ModelViewSet):
	queryset=newroom.objects.all()
	serializer_class=newroomSerializer

	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			newroom.objects.get_or_create(Name=data['Name'],defaults={'Class':data['Class'],'Section':data['Section','Awards':data['Awards'],'Description':data['Description']]})
			return Response(data)
		else:
			return Response(serializer.errors)
