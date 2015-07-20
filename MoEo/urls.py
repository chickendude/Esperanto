from django.conf.urls import url

from . import views

urlpatterns = [
#	url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
#    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
#    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

	url(r'^$', views.index, name='index'),
	url(r'^(?P<leciono_id>[0-9]+)/$', views.lesson, name='lesson'),
	url(r'^edit/$', views.edit, name='edit'),
	url(r'^edit/(?P<leciono_id>[0-9]+)/$', views.edit_lesson, name='edit_lesson'),
]
