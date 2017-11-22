# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Time, Jogador, Jogo
from .forms import GameForm
import db_setings as db_conf
from django.core import serializers
import json
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['PGBD']

def home(request):
	return render(request, 'home.html')

def club_list(request):
	  clubs = Time.objects.all().order_by('name')
	  return render(request, 'club_list.html', {'clubs' : clubs})

def new_club(request):

	if request.method == 'POST':
		form = NewClubForm(data=request.POST)
		if form.is_valid():
			club = form.save()
			club.save(using='mongodb')
			return redirect('/')
	else:
		form = NewClubForm()
	return render(request, 'new_club.html', {'form': form})

def new_player(request):
	if request.method == 'POST':
		form = NewPlayerForm(data=request.POST)
		print(form)
		if form.is_valid():
			player = form.save()
			player.save(using='mongodb')
			return redirect('/')
	else:
		form = NewPlayerForm()
	return render(request, 'new_player.html', {'form': form})

def toJson(data):
	json_ = json.dumps({'Jogo':{
						   'juiz': data['juiz'],
						   'estadio': data['estadio'],
						   'timeA':{
						   		'nomeA' : data['timeA'],
						   		"jogadores": {
							   		'jogador1' : data['jogadorA1'],
									'jogador2' : data['jogadorA2'],
									'jogador3' : data['jogadorA3'],
									'jogador4' : data['jogadorA4'],
									'jogador5' : data['jogadorA5'],
									'jogador6' : data['jogadorA6'],
									'jogador7' : data['jogadorA7'],
									'jogador8' : data['jogadorA8'],
									'jogador9' : data['jogadorA9'],
									'jogador10': data['jogadorA10'],
									'jogador11': data['jogadorA11']
						   		} 
						   },
						   'timeB':{
						   		'nomeB' : data['timeB'],
						   		'jogadores':{
						   			'jogador1' : data['jogadorB1'],
									'jogador2' : data['jogadorB2'],
									'jogador3' : data['jogadorB3'],
									'jogador4' : data['jogadorB4'],
									'jogador5' : data['jogadorB5'],
									'jogador6' : data['jogadorB6'],
									'jogador7' : data['jogadorB7'],
									'jogador8' : data['jogadorB8'],
									'jogador9' : data['jogadorB9'],
									'jogador10': data['jogadorB10'],
									'jogador11': data['jogadorB11']

						   		}
							}
						   }})

	json_dict = ast.literal_eval(json_)
	return (json_dict)


def toObj():
	collection = db['PGBD']
	cursor = collection.find({})
	#jogador = Jogador(id_club=id_timeA, name_player='LeonardoSteilHenrique', position='Centro Avante')
	for document in cursor:
		times = {'nameA' : document['Jogo']['timeA']['nomeA'], 'nameB' : document['Jogo']['timeB']['nomeB']}

		jogadores = {}

		for i in range(1,24):
			if(i < 12):
				player_number ='jogadorA' + str(i)
				jogador = 'jogador' + str(i)
				jogadores[player_number] = document['Jogo']['timeA']['jogadores'][jogador]
			if(i > 12):
				player_number ='jogadorB' + str(i - 12)
				jogador = 'jogador' + str(i - 12)
				jogadores[player_number] = document['Jogo']['timeB']['jogadores'][jogador]	

		jogo = {'juiz' : document['Jogo']['juiz'], 'estadio': document['Jogo']['estadio'],
				'timeA' : times['nameA'], 'timeB':times['nameB'], 'id' : document['_id']}

	#retornar os elemtos vindos do json
	context = { 
		'times' : times,
		'jogo'  : jogo,
		'jogadores' : jogadores
	}

	return (context)

def new_game(request):
	if request.method == 'POST':
		form = GameForm(data=request.POST)
		if form.is_valid():
			data = form.cleaned_data
				
			#TODO - pegar a posição certa do jogador
			#TODO - tentar melhorar a visualição dos dados

			if db_conf.DB_TYPE == 0:
				timeA = Time.objects.create(nome=data['timeA'])
				timeA.save()
				id_timeA = Time.objects.get(nome=data['timeA'])

				for i in range (1,12):
					jogador_numero ='jogadorA' + str(i)
					player = Jogador.objects.create(jogador_time=id_timeA, nome=data[jogador_numero], posicao='Lateral')

				timeB = Time.objects.create(nome=data['timeB'])
				timeB.save()
				id_timeB = Time.objects.get(nome=data['timeB'])

				for i in range (1,12):
					jogador_numero ='jogadorB' + str(i)
					player = Jogador.objects.create(jogador_time=id_timeB, nome=data[jogador_numero], posicao='Meio Campo')

				jogo = Jogo.objects.create(timeA=timeA, timeB=timeB, estadio=data['estadio'], juiz=data['juiz'])
				jogo.save()

			elif db_conf.DB_TYPE == 1:
				games = db.PGBD
				json = toJson(data)
				games.insert_one(json).inserted_id
			
			return redirect('/')
	else:
		form = GameForm()
	return render(request, 'new_game.html', {'form': form})

def games_list(request):
	if db_conf.DB_TYPE == 0:
		jogos = Jogo.objects.all()
		context = { 'jogos' : jogos}

	elif db_conf.DB_TYPE == 1:
		context = toObj()

	return render(request,'games_list.html', context)