from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from .models import Recipient, Category

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
        recipient = r.tweet_text
    else:
        recipient = '%s needs your support! Donate/get involved here: %s and follow @%s' % (r.name, r.url, r.twitter_handle)
        if len(recipient) > 140:
            recipient = 'Help %s with a donation here: %s and follow @%s' % (r.name, r.url, r.twitter_handle)
            if len(recipient) > 140:
                recipient = '.@%s needs your help! Donate here: %s' % (r.twitter_handle, r.url)
                if len(recipient) > 140:
                    print("Error - write some tweet text for %s" % r.name)

    context = {
        'r': recipient
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
    """
    groups = []
    cats = Category.objects.all().order_by('?')
    for c in cats:
        list_all = Recipient.objects.filter(active=True, category=c.id)
        group = []
        for r in list_all:
            u = '<a href="%s" target="new">%s</a> / <a href="https://twitter.com/%s" target="new">@%s</a>' % \
                    (r.url, r.name, r.twitter_handle, r.twitter_handle)
            group.append(u)
        g = {'category': c.name.upper(), 'urls': group}
        groups.append(g)

    context = {
        'recipient_list': groups
    }
    """

    list_all = Recipient.objects.filter(active=True).exclude(twitter_handle='@unknown').order_by('?')
    context = {
        'recipient_list': list_all
    }

    # return render(request, 'recipients/all.html', context)
    return render(request, 'recipients/index.html', context)
