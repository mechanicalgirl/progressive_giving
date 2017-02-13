from django import template
from django.utils.html import format_html

register = template.Library()

@register.simple_tag
def link_to_recipient(r, classname=""):
  print(r)
  out = format_html("""<span class="recipient__helper {}"><a class="recipient__link " href="{}" target="new">{}</a>""", classname, r.url, r.name)
  if (r.twitter_handle and r.twitter_handle != "@unknown"):
    out = out + format_html("""&nbsp;<a class="fa fa-twitter-square recipient__twitter-link" title="@{}" href="http://twitter.com/{}" target="new"><span class="u-off-screen">@{}</span></a>""", r.twitter_handle, r.twitter_handle, r.twitter_handle)
  out = out + format_html("</span>")
  return out
