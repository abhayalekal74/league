# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 06:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='league.Team'),
        ),
    ]
