from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',                            views.index,        name='home'),
    url(r'^org/(?P<slug>.+)/$',           views.by_slug,      name='by_slug'),
    url(r'^category/(?P<category>.+)/$',  views.by_cat,       name='by_cat'),
    url(r'^tweet/',                       views.tweet,        name='tweet'),
    url(r'^newsletter/',                  views.newsletter,   name='newsletter'),
    url(r'^about/',                       views.about,        name='about'),
]
