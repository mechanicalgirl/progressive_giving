from django import forms

from .models import Recipient

class RecipientModelForm( forms.ModelForm ):
    tweet_text = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Recipient
        fields = ['category', 'name', 'url', 'can_donate_to', 'twitter_handle', 'tweet_text', 'last_posted_date', 'active', 'newsletter_text', 'newsletter_sent_date', 'newsletter_active']
