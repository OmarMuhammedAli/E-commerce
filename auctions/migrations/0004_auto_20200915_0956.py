# Generated by Django 3.1 on 2020-09-15 07:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200915_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 15, 9, 56, 43, 607280)),
        ),
    ]
