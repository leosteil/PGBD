from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^club_list/$', views.club_list, name='club_list'),
    url(r'^new_club/$', views.new_club, name='new_club')
]