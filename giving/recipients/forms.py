from django import forms

from .models import Recipient

class RecipientModelForm( forms.ModelForm ):
    tweet_text = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Recipient
        fields = ['active', 'can_donate_to', 'category', 'name', 'name_slug', 'url', 'twitter_handle', 'tweet_text', 'last_posted_date', 'facebook_url', 'newsletter_text', 'newsletter_sent_date', 'newsletter_active']
