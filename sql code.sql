create database if not exists INFI_Project_21;
use INFI_Project_21;

create table if not exists Auto (
	AutoId int auto_increment unique key primary key,
	Kategorie varchar (120) ,
	Kennzeichen varchar (120) ,
    Laenge varchar (120) ,
    Breite varchar (120) ,
    Hoehe varchar (120)  
);


create table if not exists Stellplatz (
	StellplatzId int auto_increment unique key primary key,
    KategorieId int (40),
    Qualitaet varchar (120) ,
    Laenge varchar (120) ,
    Breite varchar (120) ,
    Hoehe varchar (120) ,
    constraint KategorieId_constraint FOREIGN KEY (KategorieId) REFERENCES Kategorie (KategorieId)
);



create table if not exists 	Kategorie (
	KategorieId int auto_increment unique key primary key,
	Kategoriename varchar (120) ,
    Preis int (32) ,
    Videoueberwachung int (32) ,
    Versicherung varchar (120) ,
    Farbe varchar (120) 
);

create table if not exists besetzt (
	besetztId int auto_increment unique key primary key,
    AutoId int,
    StellplatzId int,
	Anfangszeitpunkt TIMESTAMP ,
    Endzeitpunkt TIMESTAMP ,
	constraint autoID_Constraint FOREIGN KEY (AutoId) REFERENCES Auto (AutoId),
    constraint StellplatzId_Constraint FOREIGN KEY(StellplatzId) REFERENCES Stellplatz (StellplatzId)
);

	
