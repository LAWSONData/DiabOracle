# Generated by Django 5.1 on 2024-09-24 17:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_donnee_etat_de_grossesse'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='date_naissance',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='sexe',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='telephone',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
