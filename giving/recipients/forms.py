from django import forms
from django.core.exceptions import ValidationError

from .models import Recipient, SuggestedRecipient


class RecipientModelForm(forms.ModelForm):
    tweet_text = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Recipient
        fields = ['active', 'can_donate_to', 'category', 'name', 'name_slug', 'url', 'twitter_handle', 'tweet_text', 'facebook_url', 'facebook_text', 'last_posted_date', 'newsletter_text', 'newsletter_sent_date', 'newsletter_active']


class SuggestedRecipientForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
      super(SuggestedRecipientForm, self).__init__(*args, **kwargs)
      for field_name in self.fields:
        self.fields[field_name].widget.attrs['class'] = 'u-full-width'

    def clean_name(self):
        name = self.cleaned_data['name']
        if SuggestedRecipient.objects.filter(name=name).exists():
            raise ValidationError("We already have an organization with that name.")
        if Recipient.objects.filter(name=name).exists():
            raise ValidationError("We already have an organization with that name.")
        return name

    def clean_url(self):
        url = self.cleaned_data['url']
        if SuggestedRecipient.objects.filter(url=url).exists():
            raise ValidationError("We already have an organization with that url.")
        if Recipient.objects.filter(url=url).exists():
            raise ValidationError("We already have an organization with that url.")
        return url

    def clean_twitter_handle(self):
        twitter_handle = self.cleaned_data['twitter_handle']
        if SuggestedRecipient.objects.filter(twitter_handle=twitter_handle).exists():
            raise ValidationError("We already have an organization with that Twitter handle.")
        if Recipient.objects.filter(twitter_handle=twitter_handle).exists():
            raise ValidationError("We already have an organization with that Twitter handle.")
        return twitter_handle

    def clean_facebook_url(self):
        facebook_url = self.cleaned_data['facebook_url']
        if facebook_url:
            if SuggestedRecipient.objects.filter(facebook_url=facebook_url).exists():
                raise ValidationError("We already have an organization with that Facebook URL.")
            if Recipient.objects.filter(facebook_url=facebook_url).exists():
                raise ValidationError("We already have an organization with that Facebook URL.")
        return facebook_url

    class Meta:
        model = SuggestedRecipient
        fields = ('name', 'url', 'twitter_handle', 'facebook_url')
