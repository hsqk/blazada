# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-23 09:25
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20171223_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
    ]
