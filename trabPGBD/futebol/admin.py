from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Time, Jogador, Jogo
# Register your models here.

class AdminTime(ModelAdmin):
	list_display = ('nome',)
	search_fields = ('nome',)

'''class AdminJogador(ModelAdmin):
	list_display = ('name_player','position',)
	search_fields = ('name_player',)

class AdminJogo(ModelAdmin):
	list_display = ('id','id_club_home','id_club_away','stadium','refere',)
	search_fields = ('refere',)'''

admin.site.register(Time,AdminTime)
#admin.site.register(Jogador,AdminJogador)
#admin.site.register(Jogo,AdminJogo)