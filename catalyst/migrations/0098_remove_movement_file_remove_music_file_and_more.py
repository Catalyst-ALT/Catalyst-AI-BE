# Generated by Django 4.2.3 on 2023-07-26 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0097_remove_write_new_instance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movement',
            name='file',
        ),
        migrations.RemoveField(
            model_name='music',
            name='file',
        ),
        migrations.RemoveField(
            model_name='visualart',
            name='file',
        ),
        migrations.RemoveField(
            model_name='write',
            name='file',
        ),
    ]
