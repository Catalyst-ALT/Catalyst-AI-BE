# Generated by Django 4.2.3 on 2023-07-18 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0044_alter_write_prompt_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='write',
            name='input_length',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
