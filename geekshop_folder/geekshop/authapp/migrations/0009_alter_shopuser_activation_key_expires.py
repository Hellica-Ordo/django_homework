# Generated by Django 3.2 on 2022-01-23 00:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20220121_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 25, 0, 14, 37, 939020, tzinfo=utc)),
        ),
    ]
