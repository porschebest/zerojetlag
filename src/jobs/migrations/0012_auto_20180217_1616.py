# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-17 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_jobinfo_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobinfo',
            old_name='career',
            new_name='Career',
        ),
        migrations.RenameField(
            model_name='jobinfo',
            old_name='category',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='jobinfo',
            old_name='company',
            new_name='Company',
        ),
        migrations.RenameField(
            model_name='jobinfo',
            old_name='deadLine',
            new_name='DeadLine',
        ),
        migrations.RenameField(
            model_name='jobinfo',
            old_name='interviewExp',
            new_name='InterviewExp',
        ),
        migrations.RenameField(
            model_name='jobinfo',
            old_name='jobDescription',
            new_name='JobDescription',
        ),
        migrations.RenameField(
            model_name='jobinfo',
            old_name='jobRequirements',
            new_name='JobRequirements',
        ),
        migrations.RenameField(
            model_name='jobinfo',
            old_name='jobTitle',
            new_name='JobTitle',
        ),
        migrations.RenameField(
            model_name='jobinfo',
            old_name='logo',
            new_name='Logo',
        ),
        migrations.RenameField(
            model_name='jobinfo',
            old_name='timestamp',
            new_name='Timestamp',
        ),
        migrations.RenameField(
            model_name='jobinfo',
            old_name='updated',
            new_name='Updated',
        ),
        migrations.RenameField(
            model_name='jobinfo',
            old_name='videoLink',
            new_name='VideoLink',
        ),
    ]
