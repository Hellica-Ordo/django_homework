# Generated by Django 3.2 on 2022-01-08 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='add_datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата добавления'),
        ),
    ]
