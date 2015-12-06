# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('KolaySiparisApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('joindate', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('delivertime', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant_Promos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('restaurant', models.OneToOneField(to='KolaySiparisApp.Restaurant')),
            ],
        ),
    ]
