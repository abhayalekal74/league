# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 03:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PointsOfUserPerFixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.Fixture')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('won', models.IntegerField(default=0)),
                ('lost', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('points', models.IntegerField(default=0)),
                ('calls_per_day', models.IntegerField(default=0)),
                ('group_sales', models.IntegerField(default=0)),
                ('meetings', models.IntegerField(default=0)),
                ('fse', models.IntegerField(default=0)),
                ('five_match_plan', models.IntegerField(default=0)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.Team')),
            ],
        ),
        migrations.AddField(
            model_name='pointsofuserperfixture',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.User'),
        ),
        migrations.AddField(
            model_name='fixture',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='league.Team'),
        ),
        migrations.AddField(
            model_name='fixture',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='league.Team'),
        ),
        migrations.AddField(
            model_name='fixture',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.Team'),
        ),
    ]
