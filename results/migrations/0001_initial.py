# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 08:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('exam_code', models.CharField(max_length=15)),
                ('exam_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'exams',
            },
        ),
        migrations.CreateModel(
            name='ResultsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=11)),
                ('student_id', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('dept', models.CharField(max_length=3)),
                ('marks', models.DecimalField(decimal_places=2, max_digits=4)),
                ('batch', models.IntegerField()),
                ('exam_id', models.ForeignKey(db_column='exam_id', on_delete=django.db.models.deletion.CASCADE, to='results.ExamInfo')),
            ],
            options={
                'db_table': 'results_info',
            },
        ),
    ]
