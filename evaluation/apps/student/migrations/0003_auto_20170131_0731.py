# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='marks',
            field=models.IntegerField(),
        ),
    ]
