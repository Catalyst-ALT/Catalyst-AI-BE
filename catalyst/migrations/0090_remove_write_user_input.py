# Generated by Django 4.2.3 on 2023-07-25 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0089_write_user_input'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='write',
            name='user_input',
        ),
    ]
