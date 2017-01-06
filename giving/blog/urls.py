from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',                        views.list_all,    name='blog_home'),
    url(r'^post/(?P<title>.*?)/*$',   views.view_post,   name='post_view'),
]
