# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectsinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='subjectsinfo',
            name='subject_code',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
