-- drop database trab;
create database trab;
use trab;

create table Club(
id_club int auto_increment,
nome_club char(30),
primary key (id_club)
);

create table Jogador(
id_jogador int auto_increment,
id_club int,
nome_jog char(30),
posicao enum('goleiro','lateral','zagueiro','meio-campo','atacante','tecnico'),
primary key (id_jogador),
foreign key (id_club) references Club(id_club)
);

create table Jogo(
id_jogo int auto_increment,
id_club_home int,
id_club_away int,
estadio char(30),
arbitro char(30),
primary key (id_jogo),
foreign key(id_club_home) references Club(id_club),
foreign key(id_club_away) references Club(id_club)
);

insert into Club (nome_club) values ('Grêmio'),('Inter');
select * from Club;
insert into Jogador (id_club,nome_jog,posicao) values (1,'Grohe','goleiro');
insert into Jogador (id_club,nome_jog,posicao) values (2,'Danilo','goleiro');
insert into Jogador (id_club,nome_jog,posicao) values (1,'Edilson','lateral');
insert into Jogador (id_club,nome_jog,posicao) values (1,'Luan','atacante');
insert into Jogo (id_club_home, id_club_away, estadio, arbitro) values (1,2,'Arena do Grêmio','Vuaden');

select * from Jogo natural join (Club);