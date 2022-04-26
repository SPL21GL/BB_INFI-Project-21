# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Auto(db.Model):
    __tablename__ = 'auto'

    AutoId = db.Column(db.Integer, primary_key=True, unique=True)
    Kategorie = db.Column(db.String(120))
    Kennzeichen = db.Column(db.String(120))
    Laenge = db.Column(db.String(120))
    Breite = db.Column(db.String(120))
    Hoehe = db.Column(db.String(120))



class Besetzt(db.Model):
    __tablename__ = 'besetzt'

    besetztId = db.Column(db.Integer, primary_key=True, unique=True)
    AutoId = db.Column(db.ForeignKey('auto.AutoId'), index=True)
    StellplatzId = db.Column(db.ForeignKey('stellplatz.StellplatzId'), index=True)
    Anfangszeitpunkt = db.Column(db.DateTime)
    Endzeitpunkt = db.Column(db.DateTime)

    auto = db.relationship('Auto', primaryjoin='Besetzt.AutoId == Auto.AutoId', backref='besetzts')
    stellplatz = db.relationship('Stellplatz', primaryjoin='Besetzt.StellplatzId == Stellplatz.StellplatzId', backref='besetzts')



class Kategorie(db.Model):
    __tablename__ = 'kategorie'

    KategorieId = db.Column(db.Integer, primary_key=True, unique=True)
    Kategoriename = db.Column(db.String(120))
    Preis = db.Column(db.Integer)
    Videoueberwachung = db.Column(db.Integer)
    Versicherung = db.Column(db.String(120))
    Farbe = db.Column(db.String(120))



class Stellplatz(db.Model):
    __tablename__ = 'stellplatz'

    StellplatzId = db.Column(db.Integer, primary_key=True, unique=True)
    KategorieId = db.Column(db.ForeignKey('kategorie.KategorieId'), index=True)
    Qualitaet = db.Column(db.String(120))
    Laenge = db.Column(db.String(120))
    Breite = db.Column(db.String(120))
    Hoehe = db.Column(db.String(120))

    kategorie = db.relationship('Kategorie', primaryjoin='Stellplatz.KategorieId == Kategorie.KategorieId', backref='stellplatzzes')
