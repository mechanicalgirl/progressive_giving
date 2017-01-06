from django.contrib import admin

from .models import Post
from recipients.models import Recipient

class PostAdmin(admin.ModelAdmin):

    def related_recipient_text(self, obj):
        return obj.recipient.newsletter_text

    def recipient_body_active(self, obj):
        if obj.recipient.newsletter_active:
            return True
        else:
            return False

    recipient_body_active.boolean = True
    list_display = ('title', 'publish', 'created_at', 'recipient_body_active')
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('related_recipient_text',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['recipient'].queryset = Recipient.objects.all().order_by('name')
        return form

admin.site.register(Post, PostAdmin)
