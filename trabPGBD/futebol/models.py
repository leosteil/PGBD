from django.db import models
from django.utils import timezone
# Create your models here.

class Club(models.Model):
	name = models.CharField(max_length = 100)

	def publish(self):
		self.save()

	def __str__(self):
		return (self.name)

class Jogador(models.Model):
	PLAYER_POSITION = (
		('goleiro','goleiro'), ('lateral','lateral'), ('zagueiro','zagueiro'),('meio-campo','meio-campo'),('atacante','atacante'), ('tecnico','tecnico')
	)
	name_player = models.CharField(max_length = 50)
	id_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='club_id',verbose_name='Clube')
	position = models.CharField(
		max_length = 15,
		choices = PLAYER_POSITION,
		verbose_name = 'Posição',
		)

	def publish(self):
		self.save()

class Jogo(models.Model):
	id_club_home = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='id_club_home',verbose_name='Local')
	id_club_away = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='id_club_away',verbose_name='Visitante')
	stadium = models.CharField(max_length = 50)
	refere = models.CharField(max_length = 30)

	def publish(self):
		self.save()