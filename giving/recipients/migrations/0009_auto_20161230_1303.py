# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipients', '0008_recipient_name_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipient',
            name='tweet_text',
            field=models.CharField(blank=True, max_length=135, null=True),
        ),
    ]
