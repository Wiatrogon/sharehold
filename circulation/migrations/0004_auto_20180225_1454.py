# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-25 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulation', '0003_auto_20180225_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentalclient',
            old_name='name',
            new_name='initials',
        ),
    ]