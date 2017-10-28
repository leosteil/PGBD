from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import NewClubForm



def home(request):
	return render(request, 'home.html')

def club_list(request):
	return render(request,'club_list.html', {})

def new_club(request):

	if request.method == 'POST':
		form = NewClubForm(data=request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('/')
	else:
		form = NewClubForm()
	return render(request, 'new_club.html', {'form': form})