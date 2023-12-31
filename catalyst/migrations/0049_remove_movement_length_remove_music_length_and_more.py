# Generated by Django 4.2.3 on 2023-07-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0048_alter_visualart_prompt_length'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movement',
            name='length',
        ),
        migrations.RemoveField(
            model_name='music',
            name='length',
        ),
        migrations.AddField(
            model_name='movement',
            name='input_length',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='movement',
            name='prompt_length',
            field=models.CharField(choices=[('one word', 'one word'), ('three words', 'three words'), ('prompt', 'prompt')], default='prompt'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='music',
            name='input_length',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='music',
            name='prompt_length',
            field=models.CharField(choices=[('one word', 'one word'), ('three words', 'three words'), ('prompt', 'prompt')], default='prompt'),
            preserve_default=False,
        ),
    ]
