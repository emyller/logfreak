# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 01:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_logger', '0002_smsentry_verbose_names'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smsentry',
            old_name='type',
            new_name='_type',
        ),
    ]
