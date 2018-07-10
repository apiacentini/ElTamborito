# Generated by Django 2.0.7 on 2018-07-10 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acquista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantita', models.PositiveIntegerField()),
                ('prezzo', models.FloatField()),
                ('data', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Gestore',
            fields=[
                ('user', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Indirizzo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazione', models.CharField(max_length=50)),
                ('citta', models.CharField(max_length=50)),
                ('via', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=50)),
                ('CAP', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Prodotto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anno', models.DateField()),
                ('tipologia', models.CharField(max_length=100)),
                ('modello', models.CharField(max_length=100)),
                ('prezzo', models.FloatField()),
                ('disponibilita', models.BooleanField()),
                ('caratteristiche', models.CharField(choices=[('1', 'Nuovo'), ('2', 'Usato')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Utente',
            fields=[
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('cognome', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('indirizzo', models.ManyToManyField(to='eltambo.Indirizzo')),
            ],
        ),
        migrations.AddField(
            model_name='prodotto',
            name='acquistato',
            field=models.ManyToManyField(through='eltambo.Acquista', to='eltambo.Utente'),
        ),
        migrations.AddField(
            model_name='acquista',
            name='prodotto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eltambo.Prodotto'),
        ),
        migrations.AddField(
            model_name='acquista',
            name='utente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eltambo.Utente'),
        ),
    ]