from django.conf.urls import patterns, url

from maps import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<trip_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
)