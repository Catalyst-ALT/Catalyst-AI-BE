# Generated by Django 4.2.3 on 2023-07-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0054_remove_music_movement_remove_music_visual_art_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='temperature',
            field=models.FloatField(default=0.8),
        ),
        migrations.AlterField(
            model_name='music',
            name='temperature',
            field=models.FloatField(default=0.8),
        ),
    ]
