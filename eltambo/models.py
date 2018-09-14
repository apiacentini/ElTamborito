from django.db import models
from django.contrib.auth.models import AbstractUser



class Indirizzo (models.Model):
    nazione = models.CharField(max_length=50)
    citta = models.CharField(max_length=50)
    via = models.CharField(max_length=100)
    provincia = models.CharField(max_length=50)
    CAP = models.CharField(max_length=5)


    def __str__(self):
        return self.via


class Utente (AbstractUser):
    indirizzo = models.ManyToManyField('Indirizzo',  blank=True, symmetrical=False)


class Prodotto (models.Model):
    CARATTERISTICHE_PRODOTTO = (
        ('1', 'Nuovo'),
        ('2', 'Usato'),
        ('3', 'Nuovo-scontato'),
        ('4', 'Usato-scontato'),
    )
    acquistato = models.ManyToManyField(Utente, through='Acquista')
    anno = models.DateField()
    tipologia = models.CharField(max_length=100)
    modello = models.CharField(max_length=100)
    prezzo = models.FloatField()
    disponibilita = models.BooleanField()
    caratteristiche = models.CharField(max_length=5, choices=CARATTERISTICHE_PRODOTTO)
    img = models.URLField()


class Acquista (models.Model):
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    quantita = models.PositiveIntegerField()
    prezzo = models.FloatField()
    data = models.DateTimeField()

    def __str__(self):
        return self.prodotto.modello


class Ricavo (models.Model):
    totale = models.FloatField()

    def __str__(self):
        return self.totale

