from django.contrib import admin

from .models import Amount

class AmountAdmin(admin.ModelAdmin):
    list_display = ('donation_date', 'recipient', 'amount')
    ordering = ('-donation_date',)
    # form = RecipientModelForm

admin.site.register(Amount, AmountAdmin)
