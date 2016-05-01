# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 06:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_field_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactphone',
            name='msisdn',
            field=models.CharField(help_text='The phone number, including country code. Digits only.', max_length=15, validators=[django.core.validators.MinLengthValidator(9), django.core.validators.RegexValidator('^\\d+$')], verbose_name='MSISDN (number)'),
        ),
    ]
