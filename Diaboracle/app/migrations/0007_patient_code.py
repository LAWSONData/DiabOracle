# Generated by Django 5.1 on 2024-09-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_patient_date_naissance_patient_sexe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='code',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
