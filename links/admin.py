from django.contrib import admin
from .models import ShortLink


@admin.register(ShortLink)
class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'original_url', 'user', 'created_at')
    search_fields = ('short_code', 'original_url', 'user__username')

