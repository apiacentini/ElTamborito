from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Utente)
admin.site.register(Prodotto)
admin.site.register(Indirizzo)
admin.site.register(Acquista)
admin.site.register(Ricavo)