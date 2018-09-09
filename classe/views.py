'''from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

class classeViewsets(viewsets.ModelViewSet):
	queryset=classe.objects.all()
	serializer_class=classeSerializer
	



	# def create(self,request):
	#  	classes=classe.objects.all()
	#  	serializer=classeSerializer(classes)

	# 	return Response(serializer.data)

	def create(self, request):

		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid():
			data = serializer.data
			classe.objects.get_or_create(Class=data['Class'], defaults={'Section':data['Section'], 'Capacity':data['Capacity'], 'No_of_Students':data['No_of_Students']})
			return Response(data)

		else:
			return Response(serializer.errors)


	def get(self, request, pk, format=None):
		classe = self.get_object(pk)
		serializer = classeSerializer(classe)
		return Response(serializer.data)

	def retrieve(self, request, pk):
		classe = classe.objects.get(id=pk)
		serializer = self.get_serializer(data=classes)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		classe = self.get_object(pk)
		serializer = classeSerializer(classe, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		classe = self.get_object(pk)
		classe.objects.get(pk=pk).delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

'''

from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework import serializers
from .models import *
from .serializers import *
from rest_framework import request
from rest_framework.response import Response
from rest_framework import generics







class classeList(generics.ListCreateAPIView):
	queryset = classe.objects.all()
	serializer_class = classeSerializer


class classeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = classe.objects.all()
	serializer_class = classeSerializer

