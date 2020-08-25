from rest_framework import serializers
from billspayable.models.models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__' # ['id', 'seller', 'invoice_no', 'linenos', 'language', 'style']

