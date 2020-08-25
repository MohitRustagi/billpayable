from django.db import models

class DocumentUploadStatus:
    PENDING_VERIFICATION = 1
    APPROVED = 2
    REJECTED = 3
    EDITED_AND_APPROVED = 4

DOCUMENT_UPLOAD_STATUS_CHOICES = [
    (DocumentUploadStatus.APPROVED, 'Approved'),
    (DocumentUploadStatus.REJECTED, 'Rejected'),
    (DocumentUploadStatus.EDITED_AND_APPROVED, 'Edited and approved'),
    (DocumentUploadStatus.PENDING_VERIFICATION, 'Pending'),
]

class Seller(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Buyer(models.Model):
    name = models.CharField(max_length=255, unique=True)



class Invoice(models.Model):
    status = models.IntegerField(
        choices=DOCUMENT_UPLOAD_STATUS_CHOICES,
        default=DocumentUploadStatus.PENDING_VERIFICATION)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=255)
    due_date = models.DateField()
    description = models.CharField(default='', max_length=255)
    price = models.DecimalField(default=0.0, max_digits=19, decimal_places=2)
    qty = models.FloatField(default=0.0)
    amount = models.DecimalField(default=0.0, max_digits=19, decimal_places=2)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    tax_perc = models.DecimalField(default=0, max_digits=19, decimal_places=1)
    # System Generated ID at invoice level.
    invoice_id = models.CharField(default='',
        max_length=64, null=False, blank=False)
    
    def __str__(self):
        return str(self.invoice_no)