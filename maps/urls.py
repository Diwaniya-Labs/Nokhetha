from django.conf.urls import patterns, url

from maps import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^nokhethas', views.nokhethas, name='nokhthas'),
    url(r'^(?P<trip_id>\d+)/$', views.detail, name='detail'),
    url(r'^nokhetha/(?P<nokh_id>\d+)/$', views.nokhetha_detail, name='nokhetha_detail'),
    # ex: /polls/5/results/
)