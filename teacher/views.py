'''from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework import status

class teacherViewsets(viewsets.ModelViewSet):
	queryset=teacher.objects.all()
	serializer_class=teacherSerializer


	def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			teacher.objects.get_or_create(Name=data['Name'],defaults={'Subjects':data['Subjects'],'Extras':data['Extras'],'Payments':data['Payments'],'Classes':data['Classes']})
			return Response(data)
		else:
			return Response(serializer.errors)
	def get (self,request,pk,format=None):
		tec=teacher.objects.get(id=pk)
		serializer = self.get_serializer(data=tec)
		serializer.is_valid()
		return Response(serializer.data)

	def retrieve(self, request, pk):
		obj = self.get_object()
		return Response({obj.Name,obj.Subjects,obj.Classes})


	def update(self,request, pk):
		serializer=self.get_serializer(data=request.data)
		data = {}
		if serializer.is_valid():
			data=serializer.data
		
			obj = self.get_object()

			obj.Name = data['Name']
			obj.Subjects=data['Subjects']
			obj.Extras=data['Extras']
			obj.Payments=data['Payments']
			obj.Classes=data['Classes']

			obj.save()

		return Response(data)


	def delete(self,request,pk,format=None):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			teacher.objects.get(pk=pk).delete()	

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







class teacherList(generics.ListCreateAPIView):
	queryset = teacher.objects.all()
	serializer_class = teacherSerializer


class teacherDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = teacher.objects.all()
	serializer_class = teacherSerializer

