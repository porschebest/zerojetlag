# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-02-16 12:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20180216_1245'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CompanyName',
            new_name='Jobs',
        ),
        migrations.RenameField(
            model_name='jobs',
            old_name='name',
            new_name='jobTitle',
        ),
    ]
