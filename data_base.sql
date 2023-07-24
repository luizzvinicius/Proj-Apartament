create table if not exists Proprietario(
	cpf varchar(11),
	nome varchar(50) not null,
	telefone varchar(11) not null,
	data_cadastro date,
	primary key (cpf)
);
create table if not exists Apartamento(
	numero varchar(5),
	data_cadastro date,
	cpf varchar(11),
	primary key (numero),
	foreign key (cpf) references Proprietario(cpf) on delete cascade
);
create table if not exists Pessoa(
	cpf varchar(11),
	nome varchar(50) not null,
	telefone varchar(11) not null,
	data_cadastro date,
	num_apto varchar(5),
	primary key (cpf),
	foreign key (num_apto) references Apartamento(numero) on delete cascade
);
create table if not exists Veiculo(
	placa varchar(7),
	categoria varchar(5) not null,
	cor varchar(20),
	modelo varchar(20) not null,
	observacao varchar(50),
	num_apto varchar(5),
	data_cadastro date,
	primary key (placa),
	foreign key (num_apto) references Apartamento(numero) on delete cascade
)