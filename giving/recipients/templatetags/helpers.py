from django import template
from django.utils.html import format_html

import re
import pyphen

pyphen.language_fallback('en_US')
dic = pyphen.Pyphen(lang='en_US')

register = template.Library()

@register.simple_tag
def link_to_recipient(r, classname=""):
  url = '/org/%s/' % r.name_slug
  out = format_html(u"""<span class="recipient__helper {}"><a class="recipient__link " href="{}">{}</a>""", classname, url, r.name)

  # Twitter
  if r.twitter_handle and r.twitter_handle != "@unknown":
    out += format_html(u"""&nbsp;<a class="fa fa-twitter-square recipient__twitter-link" title="@{}" href="http://twitter.com/{}" target="new"><span class="u-off-screen">@{}</span></a>""", r.twitter_handle, r.twitter_handle, r.twitter_handle)

  # Facebook
  if r.facebook_url:
    out += format_html(u"""<a class="fa fa-facebook-square recipient__facebook-link" href="{}" target="new"><span class="u-off-screen">Facebook page for {}</span></a>""", r.facebook_url, r.name)
  

  out += format_html(u"</span>")
  return out
  

@register.simple_tag
def mark_for_hyphenation(text):
  words = text.split(' ')
  hyphenated_words = [choose_hyphens(word) for word in words]
  return format_html( ' '.join(hyphenated_words) )
  
def choose_hyphens(word):
  hyph = dic.inserted(word, '-')
  # Remove the last hyphen unless there are at least 4 letters after it.
  # Otherwise we get stuff like:
  #       humanitari-
  #       an
  if (len(word) > 6) and (not re.search('-\\w{4,}$', hyph)):
    hyph = re.sub('-(\\w+)$', '\\1', hyph)
  
  return re.sub('-', '&shy;', hyph)
