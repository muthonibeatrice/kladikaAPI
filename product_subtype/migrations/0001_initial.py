# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-28 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtypes', models.CharField(choices=[(b'suits', b'Suits'), (b'khaki_pants', b'Khaki_pants'), (b'accessories', b'Accessories'), (b'shirts', b'Shirts'), (b'dresses', b'Dresses'), (b'tops', b'Tops'), (b'skirts', b'Skirts'), (b'jeans', b'Jeans'), (b'jewellery', b'Jewellery'), (b'handbags', b'Handbags'), (b'shoes', b'Shoes')], max_length=255)),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('modifieddate', models.DateTimeField(auto_now=True)),
                ('product_typeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_type.ProductType')),
            ],
        ),
    ]