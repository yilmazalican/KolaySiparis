# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KolaySiparisApp', '0003_order_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.CharField(default='Nakit', max_length=100),
        ),
    ]
