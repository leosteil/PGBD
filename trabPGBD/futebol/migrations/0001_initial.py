# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name_player', models.CharField(max_length=50)),
                ('position', models.CharField(verbose_name='Posição', choices=[('goleiro', 'goleiro'), ('lateral', 'lateral'), ('zagueiro', 'zagueiro'), ('meio-campo', 'meio-campo'), ('atacante', 'atacante'), ('tecnico', 'tecnico')], max_length=15)),
                ('id_club', models.ForeignKey(related_name='club_id', verbose_name='Clube', to='futebol.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('stadium', models.CharField(max_length=50)),
                ('refere', models.CharField(max_length=30)),
                ('id_club_away', models.ForeignKey(related_name='id_club_away', verbose_name='Visitante', to='futebol.Club')),
                ('id_club_home', models.ForeignKey(related_name='id_club_home', verbose_name='Local', to='futebol.Club')),
            ],
        ),
    ]
