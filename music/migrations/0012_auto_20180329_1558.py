# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-03-29 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=500)),
                ('message', models.CharField(max_length=10000)),
            ],
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
