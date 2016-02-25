# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-19 16:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20160219_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskassignment',
            name='correct_answer',
        ),
        migrations.AddField(
            model_name='answeroption',
            name='correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='taskassignment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='tasks.Task'),
        ),
    ]
