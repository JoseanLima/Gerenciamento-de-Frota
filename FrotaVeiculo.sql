create database FrotaVeiculo;
drop database if exists FrotaVeiculo;
use FrotaVeiculo;

-- °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°° TABELAS °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
create table veiculo
(
	idVeiculo int primary key auto_increment,
    placa varchar(7) not null,
    modelo varchar(50) not null,
    ano varchar(4) not null
);

create table rota
(
	idRota int primary key auto_increment,
    descricao varchar(255) not null,
    idVeiculo int, -- referenciando chave estrangeira
    constraint fk_rota_veiculo foreign key (idVeiculo) references veiculo(idVeiculo) -- criando chave estrangeira para veiculo
);

create  table manutencao
(
	idManutencao int primary key auto_increment,
    descricao varchar(255) not null,
    data varchar(10) not null,
    idVeiculo int, -- referenciando chave estrangeira
    constraint fk_manutencao_veiculo foreign key (idVeiculo) references veiculo(idVeiculo) -- criando chave estrangeira para veiculo
);

-- °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°° INSERINDO DADOS °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

-- °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°° CONSULTAS °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

select * from veiculo;