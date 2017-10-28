from django.shortcuts import render

def club_list(request):
	return render(request,'futebol/club_list.html', {})