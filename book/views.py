from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework import serializers
from .models import *
from .serializers import *
from rest_framework import request
from rest_framework.response import Response
from rest_framework import generics







class bookList(generics.ListCreateAPIView):
	queryset = book.objects.all()
	serializer_class = bookSerializer


class bookDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = book.objects.all()
	serializer_class = bookSerializer


# Create your views here.


