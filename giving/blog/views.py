from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from recipients.models import Recipient, Category
from .models import Post

def list_all(request):
    """
    """
    list_all = Post.objects.filter(publish=True).order_by('-created_at')
    context = {
        'latest_entry': list_all[0],
        'older_entries': list_all[1:],
        'url': request.META['QUERY_STRING'],
    }
    return render(request, 'blog/all.html', context)

def view_post(request, title):
    """
    """
    try:
        entry = Post.objects.get(slug=title, publish=True)
    except ObjectDoesNotExist:
        entry = None

    body = ''
    if entry:
        body = entry.recipient.newsletter_text

    context = {
        'entry': entry,
        'entry_body': body,
        'url': request.META['QUERY_STRING'],
    }
    return render(request, 'blog/view_post.html', context)
