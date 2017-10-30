from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Club, Jogador, Jogo
# Register your models here.

class AdminClub(ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)

class AdminJogador(ModelAdmin):
	list_display = ('name_player','position',)
	search_fields = ('name_player',)

class AdminJogo(ModelAdmin):
	list_display = ('id','id_club_home','id_club_away','stadium','refere',)
	search_fields = ('refere',)

admin.site.register(Club,AdminClub)
admin.site.register(Jogador,AdminJogador)
admin.site.register(Jogo,AdminJogo)