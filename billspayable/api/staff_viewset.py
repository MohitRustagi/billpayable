import random
import uuid

from billspayable.api.invoice_serializer import InvoiceSerializer
from billspayable.models.models import Invoice, Seller, Buyer, DocumentUploadStatus
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from billspayable.api import user_viewset_utils as user_utils

@action(detail=True, methods=['patch'])
class StaffViewset(viewsets.ViewSet):
    """
    Assumption 1 - User is authorized and authenticated.
    Assumption 2 - If document is approved, it is digitized.
    It has API/functions for staff users-
    Edit invoice details.
    """
    queryset = Invoice.objects.all()
    def partial_update(self, request, pk=None):
        invoice =  get_object_or_404(self.queryset, pk=pk)
        serializer = InvoiceSerializer(
           invoice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data=serializer.data)
        return Response(status=400, data="wrong parameter..")


