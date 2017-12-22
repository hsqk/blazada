from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.trackee_new, name='trackee_new'),
]


