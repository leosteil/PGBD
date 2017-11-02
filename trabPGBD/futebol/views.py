from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Club
from .forms import NewClubForm, NewPlayerForm, NewGameForm



def home(request):
	return render(request, 'home.html')

def club_list(request):
      clubs = Club.objects.all().order_by('name')
      return render(request, 'club_list.html', {'clubs' : clubs})

def new_club(request):

	if request.method == 'POST':
		form = NewClubForm(data=request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('/')
	else:
		form = NewClubForm()
	return render(request, 'new_club.html', {'form': form})

def new_player(request):

	if request.method == 'POST':
		form = NewPlayerForm(data=request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('/')
	else:
		form = NewPlayerForm()
	return render(request, 'new_player.html', {'form': form})

def new_game(request):

	if request.method == 'POST':
		form = NewGameForm(data=request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('/')
	else:
		form = NewGameForm()
	return render(request, 'new_game.html', {'form': form})