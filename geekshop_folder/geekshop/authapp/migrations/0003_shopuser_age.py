# Generated by Django 3.2 on 2021-12-23 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_remove_shopuser_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(default=25, verbose_name='возраст'),
            preserve_default=False,
        ),
    ]