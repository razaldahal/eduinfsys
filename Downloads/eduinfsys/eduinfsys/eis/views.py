# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets

from eis.serializers import studentSerializer,gradeSerializer,teacherSerializer
from eis.models import student,grade,teacher


class studentViewset(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer

    
        
class gradeViewset(viewsets.ModelViewSet):
    queryset = grade.objects.all()
    serializer_class = gradeSerializer
# Create your views here.
class teacherViewset(viewsets.ModelViewSet):
    queryset = teacher.objects.all()
    serializer_class = teacherSerializer