# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-25 08:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
