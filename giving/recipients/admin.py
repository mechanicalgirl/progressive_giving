from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Recipient, SuggestedRecipient
from .forms import RecipientModelForm

class SuggestedRecipientAdmin(admin.ModelAdmin):
    ordering = ('-date_created',)

class RecipientAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'last_posted_date', 'active', 'can_donate_to', 'has_tw_handle', 'has_fb_url', 'is_news_active')
    list_filter = ('category', )
    ordering = ('-last_posted_date',)
    search_fields = ('name',)
    form = RecipientModelForm
    prepopulated_fields = {"name_slug": ("name",)}

    def has_tw_handle(self, obj):
        color = 'no'
        if obj.twitter_handle and obj.twitter_handle != '@unknown':
            color = 'yes'
        return format_html('<img src="/static/admin/img/icon-{}.svg" alt="True" data-pin-nopin="true">', color)
    has_tw_handle.short_description = 'TW'
    has_tw_handle.admin_order_field = 'tweet_text'

    def has_fb_url(self, obj):
        color = 'no'
        if obj.facebook_url:
            color = 'yes'
        return format_html('<img src="/static/admin/img/icon-{}.svg" alt="True" data-pin-nopin="true">', color)
    has_fb_url.short_description = 'FB'
    has_fb_url.admin_order_field = 'facebook_url'

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
    is_fb_text.short_description = 'FBT'
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
admin.site.register(SuggestedRecipient, SuggestedRecipientAdmin)
