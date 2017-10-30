from django.db import models
from django.utils import timezone
# Create your models here.

class Club(models.Model):
	class Meta:
            ordering = ('name',)

	name = models.CharField(max_length = 100, unique=True)

	def publish(self):
		self.save()

	def __str__(self):
		return (self.name)

class Jogador(models.Model):
	PLAYER_POSITION = (
		('goleiro','Goleiro'), ('lateral','Lateral'), ('zagueiro','Zagueiro'),('meio-campo','Meio-campo'),('atacante','Atacante'), ('tecnico','Tecnico')
	)
	name_player = models.CharField(max_length = 50, verbose_name = 'Nome do Jogador')
	id_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='club_id',verbose_name='Clube')
	position = models.CharField(
		max_length = 15,
		choices = PLAYER_POSITION,
		verbose_name = 'Posição',
		)

	def publish(self):
		self.save()

class Jogo(models.Model):
	class Meta:
		ordering = ('id',)
		
	id_club_home = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='id_club_home',verbose_name='Mandante')
	id_club_away = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='id_club_away',verbose_name='Visitante')
	stadium = models.CharField(max_length = 50, verbose_name='Estádio')
	refere = models.CharField(max_length = 30, verbose_name='Árbitro')

	def publish(self):
		self.save()