# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-03 20:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0018_auto_20180303_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgamecommodity',
            name='catalogueEntry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commodities', to='catalogue.BoardGameItem'),
        ),
        migrations.AlterField(
            model_name='boardgameitem',
            name='baseGameItem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extensions', related_query_name='basegame', to='catalogue.BoardGameItem'),
        ),
    ]