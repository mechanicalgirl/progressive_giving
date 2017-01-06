from django.db import models

from recipients.models import Recipient

class Post(models.Model):
    """
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    recipient = models.ForeignKey(Recipient)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return "/post/%s/" % self.slug

    class Meta:
        ordering = ['-created_at']
