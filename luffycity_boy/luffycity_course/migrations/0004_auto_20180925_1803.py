# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-25 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luffycity_course', '0003_auto_20180925_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetail',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='luffycity_course.Course'),
        ),
    ]
