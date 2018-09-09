from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework import serializers
from .models import *
from .serializers import *
from rest_framework import request
from rest_framework.response import Response
from rest_framework import generics









class InvoiceList(generics.ListCreateAPIView):
	queryset = Invoice.objects.all()
	serializer_class = InvoiceSerializer
	
	

class InvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Invoice.objects.all()
	serializer_class = InvoiceSerializer





from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)
class MassInvoiceView(ListBulkCreateUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = BulkInvSerializer


'''def create(self, request, pk=None, company_pk=None, project_pk=None):
    is_many = True if isinstance(request.data, list) else False

    serializer = self.get_serializer(data=request.data, many=is_many)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)

class FooSerializer(BulkSerializerMixin, ModelSerializer):
    class Meta(object):
        model = FooModel
        # only necessary in DRF3
        

class FooView(ListBulkCreateUpdateDestroyAPIView):
    queryset = FooModel.objects.all()
    serializer_class = FooSerializer

'''
