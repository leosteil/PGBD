# -*- coding: utf-8 -*-
from django import forms
from .models import Time, Jogador, Jogo


class GameForm(forms.Form):
	estadio = forms.CharField(label='Estádio', max_length=100)
	juiz = forms.CharField(label='Juiz', max_length=100)
	timeA = forms.CharField(label='Time A', max_length=100)
	jogadorA1 = forms.CharField(label='Goleiro', max_length=100)
	jogadorA2 = forms.CharField(label='Lateral', max_length=100)
	jogadorA3 = forms.CharField(label='Zagueiro', max_length=100)
	jogadorA4 = forms.CharField(label='Zagueiro', max_length=100)
	jogadorA5 = forms.CharField(label='Lateral', max_length=100)
	jogadorA6 = forms.CharField(label='Meio Campo', max_length=100)
	jogadorA7 = forms.CharField(label='Meio Campo', max_length=100)
	jogadorA8 = forms.CharField(label='Meio Campo', max_length=100)
	jogadorA9 = forms.CharField(label='Meio Campo', max_length=100)
	jogadorA10 = forms.CharField(label='Atacante', max_length=100)
	jogadorA11 = forms.CharField(label='Atacante', max_length=100)
	timeB = forms.CharField(label='Time B', max_length=100)
	jogadorB1 = forms.CharField(label='Goleiro', max_length=100)
	jogadorB2 = forms.CharField(label='Lateral', max_length=100)
	jogadorB3 = forms.CharField(label='Zagueiro', max_length=100)
	jogadorB4 = forms.CharField(label='Zagueiro', max_length=100)
	jogadorB5 = forms.CharField(label='Lateral', max_length=100)
	jogadorB6 = forms.CharField(label='Meio Campo', max_length=100)
	jogadorB7 = forms.CharField(label='Meio Campo', max_length=100)
	jogadorB8 = forms.CharField(label='Meio Campo', max_length=100)
	jogadorB9 = forms.CharField(label='Meio Campo', max_length=100)
	jogadorB10 = forms.CharField(label='Atacante', max_length=100)
	jogadorB11 = forms.CharField(label='Atacante', max_length=100)


'''class NewClubForm(forms.ModelForm):
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

class EditClubForm(forms.ModelForm):
	class Meta:
		model = Club
		fields = ['name']'''