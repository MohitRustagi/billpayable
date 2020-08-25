import random
import uuid

from billspayable.models.models import Invoice, Seller,\
 Buyer, DocumentUploadStatus
from django.shortcuts import get_object_or_404

def get_invoice_status(invoice_id):
    """util to get invoice status"""
    invoice_items = Invoice.objects.filter(invoice_id=invoice_id)
    if not invoice_items.exists():
        return
    pending = invoice_items.filter(
        status=DocumentUploadStatus.PENDING_VERIFICATION)
    rejected = invoice_items.filter(status=DocumentUploadStatus.REJECTED)
    
    if pending.exists():
        return {'status': DocumentUploadStatus.PENDING_VERIFICATION}
    elif rejected.exists():
        return {'status': DocumentUploadStatus.REJECTED}
    elif not invoice_items.exists():
        return
    else:
        return {'status': DocumentUploadStatus.APPROVED}

def create_invoice(uploaded_data):
    """creates new items in invoices."""
    unique_id = uuid.uuid1()
    invoice_items = []
    for item in uploaded_data:
        seller_name = item.get('seller')
        buyer_name = item.get('buyer')
        seller = Seller.objects.get_or_create(name=seller_name)[0]
        buyer = Buyer.objects.get_or_create(name=buyer_name)[0]
        item['seller'] = seller
        item['buyer'] = buyer
        item['invoice_id'] =  unique_id
        invoice_items.append(Invoice(**item))
    Invoice.objects.bulk_create(invoice_items)
