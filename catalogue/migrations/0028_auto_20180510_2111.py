# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-10 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0027_auto_20180510_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgamecommodity',
            name='catalogueEntry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commodities', to='catalogue.BoardGameItem'),
        ),
    ]
