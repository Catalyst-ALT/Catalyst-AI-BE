# Generated by Django 4.2.3 on 2023-07-17 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0035_write_remove_prompt_poem_delete_poem_delete_prompt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(choices=[('spatial awareness', 'spatial awareness'), ('emotional landscape', 'emotional landscape'), ('expressive gestures', 'expressive gestures'), ('rhythm and flow', 'rhythm and flow'), ('abstract and expression', 'abstract and expression'), ('personal narratives', 'personal narratives'), ('nature in motion', 'nature in motion'), ('cultural fusion', 'cultural fusion'), ('human connection', 'human connection')], default='', max_length=50)),
                ('somatic', models.CharField(choices=[('embodied awareness', 'embodied awareness'), ('breath and movement', 'breath and movement'), ('body-mind connection', 'body-mind connection'), ('anatomy', 'anatomy'), ('authentic movement', 'authentic movement'), ('grounding and centering', 'grounding and centering'), ('body mapping', 'body mapping'), ('mindful movement', 'mindful movement'), ('somatic imagination', 'somatic imagination')], default='', max_length=50)),
                ('sentiment', models.CharField(choices=[('harmony', 'harmony'), ('serenity', 'serenity'), ('solitude', 'solitude'), ('resilience', 'resilience'), ('wonder', 'wonder'), ('renewal', 'renewal'), ('fragility', 'fragility'), ('majesty', 'majesty'), ('transience', 'transience'), ('connection', 'connection')], default='', max_length=50)),
                ('emotion', models.CharField(choices=[('joy', 'joy'), ('courage', 'courage'), ('melancholy', 'melancholy'), ('euphoria', 'euphoria'), ('longing', 'longing'), ('hope', 'hope'), ('awe', 'awe'), ('bliss', 'bliss'), ('anguish', 'anguish'), ('grief', 'grief')], default='', max_length=50)),
                ('temperature', models.IntegerField(default=1)),
                ('output', models.TextField(blank=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movements', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]