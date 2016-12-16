from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^tweet/', views.tweet, name='tweet'),  # disable before going live?
]
