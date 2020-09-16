# Generated by Django 3.1 on 2020-09-15 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctionlisting'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 15, 9, 53, 11, 982584)),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
