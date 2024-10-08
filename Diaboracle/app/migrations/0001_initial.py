# Generated by Django 5.1 on 2024-09-19 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageVisiteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('sujet', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Donnee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('age', models.IntegerField(null=True)),
                ('poids', models.IntegerField(default=0)),
                ('taille', models.IntegerField(default=0)),
                ('etat_de_grossesse', models.IntegerField(null=True)),
                ('niveauInsuline', models.FloatField(default=0)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Resultat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pourcentage', models.FloatField(default=0)),
                ('donnee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.donnee')),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_naissance', models.DateField()),
                ('specialite', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('sexe', models.BooleanField(default=True)),
                ('password', models.CharField(max_length=100)),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profil')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='docteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.utilisateur'),
        ),
        migrations.AddField(
            model_name='donnee',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.utilisateur'),
        ),
    ]
