# Generated by Django 4.0.6 on 2022-07-24 20:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_history_delete_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]