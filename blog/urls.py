from django.http import HttpResponse
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.trackee_new, name='trackee_new'),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: ",content_type="text/plain"), name="robots_file"),
    ]


