# Generated by Django 4.1.2 on 2022-10-24 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_song_date_released'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='date_released',
            field=models.DateField(),
        ),
    ]
