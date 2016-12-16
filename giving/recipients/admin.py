from django.contrib import admin

from .models import Category, Recipient

class RecipientAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'category', 'last_posted_date', 'active')
    ordering = ('-last_posted_date',)
    search_fields = ('name',)

admin.site.register(Category)
admin.site.register(Recipient, RecipientAdmin)
