# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170226_0616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counted_thing', models.CharField(blank=True, max_length=20, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
