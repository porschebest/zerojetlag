# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-16 17:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20180216_1350'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Job',
            new_name='JobInfo',
        ),
    ]
