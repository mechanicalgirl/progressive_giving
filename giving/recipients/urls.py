from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^tweet/', views.tweet, name='tweet'),
    url(r'^newsletter/', views.newsletter, name='newsletter'),
]
