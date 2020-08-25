import random
import uuid

from billspayable.api.mock_invoice_data import dummy_data
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

class UserViewset(viewsets.ViewSet):
    """It has the following API/functions -
       TODO - support multiple pdf upload
       1. upload - User uploads an invoice.
       2. track status - User wants to know digitization status
                        of his/her invoice.
       3. invoice details - User wants structured invoice of a
                        document if digitized.
    """
    queryset = Invoice.objects.all()
    @action(detail=False, methods=['post'])
    def upload(self, file=None):
        # Assuming file has been parsed and uploaded.
        index = random.randint(0, len(dummy_data)-1)
        uploaded_data = dummy_data[index]
        user_utils.create_invoice(uploaded_data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'])
    def track_status(self, request, pk=None):
        """
        Track invoice digitization status.
        args:
            request: Http request object
            pk: System generated invoice id.
        """
        invoice_status = user_utils.get_invoice_status(pk)
        if not invoice_status:
            raise Http404
        results = { 'invoice_id': pk }
        results.update(invoice_status)
        return Response(results)
    
    def retrieve(self, request, pk=None):
        """
        Get invoice items.
        args:
            request: Http request object
            pk: System generated invoice id.
        """
        invoice_items = Invoice.objects.filter(invoice_id='5611acda-e648-11ea-9c5d-7c04d0d57546')
        invoice_items_cnt = invoice_items.count()
        if not invoice_items_cnt:
            raise Http404
        digitized_invoice_items = invoice_items.filter(
            Q(status=DocumentUploadStatus.APPROVED) |
            Q(status=DocumentUploadStatus.EDITED_AND_APPROVED))
        if invoice_items_cnt != digitized_invoice_items.count():
            return Response({ # TODO - get message from constants.py.
                'status': "Digitization for this invoice in progress."
            })
        serialized_data = InvoiceSerializer(invoice_items, many=True)
        return Response(serialized_data.data)
