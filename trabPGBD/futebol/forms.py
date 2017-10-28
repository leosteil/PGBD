from django import forms
from .models import Club, Jogador, Jogador

class NewClubForm(forms.ModelForm):

    class Meta:
        model = Club
        fields = ['name']