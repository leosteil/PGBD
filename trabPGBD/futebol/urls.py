from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^club_list/$', views.club_list, name='club_list'),
    url(r'^club_edit/(?P<idClub>\d+)/$', views.club_edit, name='club_edit'),
    url(r'^new_club/$', views.new_club, name='new_club'),
    url(r'^new_player/$', views.new_player, name='new_player'),
    url(r'^new_game/$', views.new_game, name='new_game')
]