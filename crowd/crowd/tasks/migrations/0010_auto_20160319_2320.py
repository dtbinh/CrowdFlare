# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-20 03:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_auto_20160226_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskassignment',
            name='task',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, 
                related_name='assignments', 
                to='tasks.Task'),
        ),
    ]
