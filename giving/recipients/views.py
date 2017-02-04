import facebook
import random

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Recipient, Category

def by_slug(request, slug):
    r = Recipient.objects.filter(active=True, name_slug=slug)
    context = {
        'categories': None,
        'random_recipient': r[0]
    }
    return render(request, 'recipients/slug.html', context)


def by_cat(request, category):
    r = Recipient.objects.filter(active=True, category__name=category)
    context = {
        'category': category,
        'recipients': r,
        'random_recipient': random.choice(r)
    }
    return render(request, 'recipients/category.html', context)


def tweet(request):
    last = Recipient.objects.filter(active=True).order_by('-last_posted_date')[:1]

    # first look through recipients who haven't been posted yet
    r = Recipient.objects.filter(active=True, last_posted_date=None).exclude(category=last[0].category).order_by('?')[:1]
    if r:
        r = r[0]
    else:
        # if no un-posted recipients remain, return to the regular active list
        r = Recipient.objects.filter(active=True).exclude(category=last[0].category).order_by('-last_posted_date')[:1]
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

    if r.facebook_text:
        msg = r.facebook_text
    else:
        m = ''
        if r.facebook_url:
            m += '%s needs your support! Donate here: %s and like/follow %s' % (r.name, r.url, r.facebook_url)
        else:
            if r.twitter_handle and r.twitter_handle != '@unknown':
                m += '%s needs your support! Donate here: %s and follow http://www.twitter.com/@%s' % (r.name, r.url, r.twitter_handle)
            else:
                m += '%s needs your support! Click here to donate/learn more: %s' % (r.name, r.url)
        msg = m

    print msg
    cfg = {"page_id": settings.FB_PAGE_ID, "access_token": settings.FB_ACCESS_TOKEN}
    api = get_fb_api(cfg)
    status = api.put_wall_post(msg)

    context = {
        'r': tweet_text,
        'h': r.twitter_handle
    }

    return JsonResponse(context)


def get_fb_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
      if page['id'] == cfg['page_id']:
        page_access_token = page['access_token']
    graph = facebook.GraphAPI(page_access_token)
    return graph


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
        list_all = Recipient.objects.filter(active=True, category=c.id).order_by('?')[:5]
        if list_all:  # some categories do not have active recipients
            g = {'name': c.name, 'recipients': list_all}
            groups.append(g)
            random_recipient = random.choice(list_all)

    context = {
        'categories': groups,
        'random_recipient': random_recipient
    }

    return render(request, 'recipients/index.html', context)

def about(request):
    list_all = Recipient.objects.filter(active=True)
    total = len(list_all)
    random_recipient = random.choice(list_all)
    context = {
        'random_recipient': random_recipient,
        'total_recipients': total
    }

    return render(request, 'recipients/about_page.html', context)
