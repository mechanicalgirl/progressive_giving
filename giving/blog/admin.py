from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title', 'publish', 'created_at',)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
