from django.db import models

from rest_framework import serializers
from .models import *
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)




class InvoiceSerializer(serializers.ModelSerializer):

	class Meta:
		model=Invoice
		fields=('student',
				'title',
				'description',
				'total',
				'status',
				'method',
				'date'	)


class BulkInvSerializer(BulkSerializerMixin):

	class Meta(object):
		model =Invoice
		fields= '__all__'
		list_serializer_class = BulkListSerializer


