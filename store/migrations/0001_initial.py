# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-28 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('merchant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storename', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('phonenumber', models.CharField(max_length=255)),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('modifieddate', models.DateTimeField(auto_now=True)),
                ('merchantid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant.Merchant')),
            ],
        ),
    ]