# Generated by Django 4.2.3 on 2023-07-19 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0069_alter_write_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='write',
            name='temperature',
            field=models.CharField(default=5),
        ),
    ]
