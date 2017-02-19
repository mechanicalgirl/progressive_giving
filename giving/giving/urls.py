from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^',         include('recipients.urls'),  name='index'),
    url(r'^blog/',    include('blog.urls')),
    url(r'^amounts/', include('donations.urls')),
    url(r'^admin/',   admin.site.urls),
]
