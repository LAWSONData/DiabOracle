# Generated by Django 5.1 on 2024-09-24 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_resultat_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donnee',
            name='etat_de_grossesse',
            field=models.IntegerField(default=0),
        ),
    ]
