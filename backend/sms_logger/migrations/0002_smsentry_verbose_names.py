# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 02:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_logger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smsentry',
            options={'verbose_name': 'SMS message', 'verbose_name_plural': 'SMS messages'},
        ),
    ]
