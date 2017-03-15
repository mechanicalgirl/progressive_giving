from django import template
from django.utils.html import format_html

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
