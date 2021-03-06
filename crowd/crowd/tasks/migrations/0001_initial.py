# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-11 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('question', models.CharField(max_length=1000, verbose_name='Question')),
                ('answer_1', models.CharField(max_length=255, verbose_name='Answer option 1')),
                ('answer_2', models.CharField(max_length=255, verbose_name='Answer option 2')),
                ('correct_answer', models.CharField(max_length=255, verbose_name='Correct answer')),
                ('time_answered', models.DateTimeField(null=True, verbose_name='Time of answer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
