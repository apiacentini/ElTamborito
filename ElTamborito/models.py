from django.db import models


class Indirizzo (models.Model):
    nazione = models.CharField(max_length=50)
    citta = models.CharField(max_length=50)
    via = models.CharField(max_length=100)
    provincia = models.CharField(max_length=50)
    CAP = models.CharField(max_length=5)


class Utente (models.Model):
    email = models.EmailField(max_length=100, primary_key=True)
    nome = models.CharField(max_length = 50)
    cognome = models.CharField(max_length = 50)
    password = models.CharField(max_length=100)
    indirizzo = models.ManyToManyField(Indirizzo)


class Prodotto (models.Model):
    CARATTERISTICHE_PRODOTTO = (
        ('Nuovo'),
        ('Usato'),
    )
    acquistato = models.ManyToManyField(Utente, through='Acquista')
    anno = models.DateField()
    tipologia = models.CharField(max_length=100)
    modello = models.CharField(max_length=100)
    prezzo = models.FloatField()
    disponibilita = models.BooleanField()
    caratteristiche = models.CharField(choices=CARATTERISTICHE_PRODOTTO)


class Acquista (models.Model):
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    quantita = models.PositiveIntegerField()
    prezzo = models.FloatField()
    data = models.DateTimeField()


class Gestore (models.Model):
    user = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)