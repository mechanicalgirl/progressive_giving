from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Recipient(models.Model):
    category = models.ForeignKey(Category)

    name = models.CharField(max_length=200, unique=True)
    name_slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    url = models.CharField(max_length=200)
    can_donate_to = models.BooleanField(default=True, verbose_name="Donate")

    twitter_handle = models.CharField(max_length=100)
    tweet_text = models.CharField(max_length=135, null=True, blank=True)
    last_posted_date = models.DateTimeField('date posted', null=True, blank=True)
    active = models.BooleanField(default=True)

    facebook_url = models.CharField(max_length=200, null=True, blank=True)
    facebook_text = models.TextField(null=True, blank=True)

    newsletter_text = models.TextField(null=True, blank=True)
    newsletter_sent_date = models.DateTimeField('date mailed', null=True, blank=True)
    newsletter_active = models.BooleanField(default=False)

    class Meta:
        ordering = ["last_posted_date", "name"]

    def __str__(self):
        return self.name
