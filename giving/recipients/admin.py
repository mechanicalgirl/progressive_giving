from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Recipient
from .forms import RecipientModelForm

class RecipientAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'last_posted_date', 'active', 'can_donate_to', 'is_tw_text', 'is_fb_text', 'is_news_active')
    list_filter = ('category', )
    ordering = ('-last_posted_date',)
    search_fields = ('name',)
    form = RecipientModelForm
    prepopulated_fields = {"name_slug": ("name",)}

    def is_tw_text(self, obj):
        color = 'no'
        if obj.tweet_text:
            color = 'yes'
        return format_html('<img src="/static/admin/img/icon-{}.svg" alt="True" data-pin-nopin="true">', color)
    is_tw_text.short_description = 'TW'
    is_tw_text.admin_order_field = 'tweet_text'

    def is_fb_text(self, obj):
        color = 'no'
        if obj.facebook_text:
            color = 'yes'
        return format_html('<img src="/static/admin/img/icon-{}.svg" alt="True" data-pin-nopin="true">', color)
    is_fb_text.short_description = 'FB'
    is_fb_text.admin_order_field = 'facebook_text'

    def is_news_active(self, obj):
        color = 'no'
        if obj.newsletter_active:
            color = 'yes'
        return format_html('<img src="/static/admin/img/icon-{}.svg" alt="True" data-pin-nopin="true">', color)
    is_news_active.short_description = 'NW'
    is_news_active.admin_order_field = 'newsletter_active'

admin.site.register(Category)
admin.site.register(Recipient, RecipientAdmin)
