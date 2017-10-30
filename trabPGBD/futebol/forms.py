from django import forms
from .models import Club, Jogador, Jogo

class NewClubForm(forms.ModelForm):

    class Meta:
        model = Club
        fields = ['name']

class NewPlayerForm(forms.ModelForm):
	class Meta:
		model = Jogador
		fields = ['id_club','position','name_player']

class NewGameForm(forms.ModelForm):
	class Meta:
		model = Jogo
		fields = ['id_club_home','id_club_away','stadium','refere'] 