from django.contrib import admin

from .models import Category, Recipient
from .forms import RecipientModelForm

class RecipientAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'last_posted_date', 'active', 'can_donate_to')
    list_filter = ('category', )
    ordering = ('-last_posted_date',)
    search_fields = ('name',)
    form = RecipientModelForm

admin.site.register(Category)
admin.site.register(Recipient, RecipientAdmin)
