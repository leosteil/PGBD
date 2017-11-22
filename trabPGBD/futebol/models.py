# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
# Create your models here.

class Time(models.Model):
	nome = models.CharField(max_length = 100, unique=True)

	class Meta:
		ordering = ('nome'),
		db_table = 'Time'

	def publish(self):
		self.save()

	def __str__(self):
		return (self.nome)

class Jogador(models.Model):
	POSICAO = (
		('goleiro','Goleiro'), ('lateral','Lateral'), ('zagueiro','Zagueiro'),('meio-campo','Meio-campo'),('atacante','Atacante'), ('tecnico','Tecnico')
	)
	nome = models.CharField(max_length = 50, verbose_name = 'Nome do Jogador')
	jogador_time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='club_id',verbose_name='Time')
	posicao = models.CharField(
		max_length = 15,
		choices = POSICAO,
		verbose_name = 'Posição',
		)


	class Meta:
		db_table = 'Jogador'

	def publish(self):
		self.save()

class Jogo(models.Model):	
	timeA = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='mandante',verbose_name='Mandante')
	timeB = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='visitante',verbose_name='Visitante')
	estadio = models.CharField(max_length = 50, verbose_name='Estádio')
	juiz = models.CharField(max_length = 30, verbose_name='Árbitro')

	class Meta:
		ordering = ('id'),
		db_table = 'Jogo'

	def publish(self):
		self.save()