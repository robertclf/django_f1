from django.conf.urls import url, include
from . import views

from rest_framework import routers

app_name = 'restapi'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'questions', views.QuestionViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
#	url(r'^$', views.index, name='index'),
#	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]