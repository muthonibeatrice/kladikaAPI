# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-10 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_variants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariants',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
