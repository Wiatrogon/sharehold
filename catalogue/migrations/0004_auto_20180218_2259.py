# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-18 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20180218_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgameitem',
            name='itemLabel',
            field=models.CharField(max_length=50),
        ),
    ]
