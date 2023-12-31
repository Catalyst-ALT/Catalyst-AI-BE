# Generated by Django 4.2.3 on 2023-07-23 15:45

from django.db import migrations, models
import upload_validator


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0087_rename_save_movement_save_prompt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(upload_to='uploads/', validators=[upload_validator.FileTypeValidator(allowed_types=['image/jpeg', 'image/png', 'video/mp4'])]),
        ),
    ]
