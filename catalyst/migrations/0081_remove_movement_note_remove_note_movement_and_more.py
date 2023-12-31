# Generated by Django 4.2.3 on 2023-07-20 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0080_remove_music_note_remove_note_music'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movement',
            name='note',
        ),
        migrations.RemoveField(
            model_name='note',
            name='movement',
        ),
        migrations.RemoveField(
            model_name='note',
            name='visual_art',
        ),
        migrations.RemoveField(
            model_name='note',
            name='write',
        ),
        migrations.AddField(
            model_name='music',
            name='note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='music_notes', to='catalyst.note'),
        ),
        migrations.AddField(
            model_name='note',
            name='note',
            field=models.TextField(default='this is a note'),
        ),
    ]
