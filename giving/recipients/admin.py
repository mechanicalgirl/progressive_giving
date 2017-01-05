from django.contrib import admin

from .models import Category, Recipient
from .forms import RecipientModelForm

class RecipientAdmin(admin.ModelAdmin):
    list_display = ('name', 'tweet_text', 'category', 'last_posted_date', 'active', 'newsletter_active', 'can_donate_to')
    list_filter = ('category', )
    ordering = ('-last_posted_date',)
    search_fields = ('name',)
    form = RecipientModelForm
    prepopulated_fields = {"name_slug": ("name",)}

admin.site.register(Category)
admin.site.register(Recipient, RecipientAdmin)
