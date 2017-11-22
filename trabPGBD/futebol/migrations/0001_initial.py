# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, verbose_name=b'Nome do Jogador')),
                ('posicao', models.CharField(max_length=15, verbose_name=b'Posi\xc3\xa7\xc3\xa3o', choices=[(b'goleiro', b'Goleiro'), (b'lateral', b'Lateral'), (b'zagueiro', b'Zagueiro'), (b'meio-campo', b'Meio-campo'), (b'atacante', b'Atacante'), (b'tecnico', b'Tecnico')])),
            ],
            options={
                'db_table': 'Jogador',
            },
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estadio', models.CharField(max_length=50, verbose_name=b'Est\xc3\xa1dio')),
                ('juiz', models.CharField(max_length=30, verbose_name=b'\xc3\x81rbitro')),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'Jogo',
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ('nome',),
                'db_table': 'Time',
            },
        ),
        migrations.AddField(
            model_name='jogo',
            name='timeA',
            field=models.ForeignKey(related_name='id_club_home', verbose_name=b'Mandante', to='futebol.Time'),
        ),
        migrations.AddField(
            model_name='jogo',
            name='timeB',
            field=models.ForeignKey(related_name='id_club_away', verbose_name=b'Visitante', to='futebol.Time'),
        ),
        migrations.AddField(
            model_name='jogador',
            name='jogador_time',
            field=models.ForeignKey(related_name='club_id', verbose_name=b'Time', to='futebol.Time'),
        ),
    ]
