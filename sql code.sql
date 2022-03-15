create database if not exists INFI_Project_21;
use INFI_Project_21;

create table if not exists Auto (
	AutoId int auto_increment unique key primary key,
	Kategorie varchar (120) not null,
	Kennzeichen text not null,
    Laenge text not null,
    Breite text not null,
    Hoehe text not null 
);


create table if not exists Stellplatz (
	StellplatzId int auto_increment unique key primary key,
	Kategorie varchar (120) not null,
    Qualitaet text not null,
    Laenge text not null,
    Breite text not null,
    Hoehe text not null
);



create table if not exists 	Kategorie (
	StellplatzId int auto_increment unique key primary key,
	Kategoriename varchar (120) not null,
    Preis int (32) not null,
    Videoueberwachung int (32) not null,
    Versicherung text not null,
    Farbe text not null
);

create table if not exists besetzt (
	besetztId int auto_increment unique key primary key,
    AutoId int,
    StellplatzId int,
	Anfangszeitpunkt varchar (120) not null,
    Endzeitpunkt varchar (120) not null,
	FOREIGN KEY (AutoId) REFERENCES Auto(AutoId),
    FOREIGN KEY(StellplatzId) REFERENCES Stellplatz(StellplatzId)
);

	
