import random

from django.shortcuts import render
from django.utils import timezone

from .models import Recipient, Category

def by_slug(request, slug):
    r = Recipient.objects.filter(active=True, name_slug=slug)
    context = {
        'categories': None,
        'random_recipient': r[0]
    }
    return render(request, 'recipients/index.html', context)


def tweet(request):

    r = Recipient.objects.filter(active=True, last_posted_date=None).order_by('?')[:1]
    if r:
        r = r[0]
    else:
        r = Recipient.objects.filter(active=True).order_by('-last_posted_date')[:1]
        r = r[0]

    post_to_twitter = request.GET.get('post', None)
    if post_to_twitter:
        r.last_posted_date = timezone.now()
        r.save(update_fields=["last_posted_date"])

    if r.tweet_text:
        tweet_text = r.tweet_text
    else:
        tweet_text = '%s needs your support! Donate/get involved here: %s and follow @%s' % (r.name, r.url, r.twitter_handle)
        if len(tweet_text) > 140:
            tweet_text = 'Help %s with a donation. Visit %s and follow @%s' % (r.name, r.url, r.twitter_handle)
            if len(tweet_text) > 140:
                tweet_text = '.@%s needs your help! Donate here: %s' % (r.twitter_handle, r.url)
                if len(tweet_text) > 140:
                    print("Error - write some tweet text for %s" % r.name)

    context = {
        'r': tweet_text
    }

    # to remove all dates, for cleanup if needed
    # all_dated = Recipient.objects.filter(active=True).exclude(last_posted_date=None)
    # for v in all_dated:
    #     v.last_posted_date = None
    #     v.save()

    # to add dates to all, for testing only
    # all_dated = Recipient.objects.filter(active=True, last_posted_date=None)
    # for v in all_dated:
    #     v.last_posted_date = timezone.now()
    #     v.save()

    return render(request, 'recipients/one.html', context)


def newsletter(request):

    r = Recipient.objects.filter(newsletter_active=True, newsletter_sent_date=None)[:1]
    if r:
        r = r[0]
        send = request.GET.get('send', None)
        if send:
            r.newsletter_sent_date = timezone.now()
            r.save()
        text = r.newsletter_text
    else:
        text = None

    context = {
        'r': text
    }

    return render(request, 'recipients/newsletter.html', context)


def index(request):
    groups = []
    cats = Category.objects.all().order_by('?')
    for c in cats:
        list_all = Recipient.objects.filter(active=True, category=c.id).order_by('name')
        if list_all:  # some categories do not have active recipients
            g = {'name': c.name, 'recipients': list_all}
            groups.append(g)
            random_recipient = random.choice(list_all)

    context = {
        'categories': groups,
        'random_recipient': random_recipient
    }

    return render(request, 'recipients/index.html', context)
