# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-08 21:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160207_2323'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AmazonWorker',
        ),
    ]
