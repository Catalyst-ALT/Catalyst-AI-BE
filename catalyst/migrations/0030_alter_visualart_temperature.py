# Generated by Django 4.2.3 on 2023-07-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0029_alter_visualart_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visualart',
            name='temperature',
            field=models.CharField(default='1'),
        ),
    ]