# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-10 15:16
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmm', '0002_auto_20161207_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hmm',
            name='ems',
        ),
        migrations.RemoveField(
            model_name='hmm',
            name='trans',
        ),
        migrations.AddField(
            model_name='hmm',
            name='gold_ratio',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='hmm',
            name='json_model',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
