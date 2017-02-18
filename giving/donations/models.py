from __future__ import unicode_literals

from django.db import models

class Amount(models.Model):
    donation_date = models.DateField('donation date', null=True, blank=True)
    recipient = models.CharField(max_length=200, null=True, blank=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ["donation_date", "recipient"]
