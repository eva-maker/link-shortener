from django.db import models
from django.contrib.auth.models import User


class ShortLink(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='short_links',
        verbose_name='User'
    )
    original_url = models.URLField('Long link')
    short_code = models.SlugField(
        'Short name',
        max_length=50,
        unique=True,
        help_text='Unique name, which will be in a short code'
    )
    created_at = models.DateTimeField('Creation date', auto_now_add=True)

    class Meta:
        verbose_name = 'Short link'
        verbose_name_plural = 'Short links'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.short_code} → {self.original_url}'
