# Generated by Django 5.2.1 on 2025-05-30 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saportfolio', '0006_disponibilite_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='disponibilite',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='disponibilite',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
