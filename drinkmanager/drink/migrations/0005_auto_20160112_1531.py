# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0004_auto_20160112_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='photo',
            field=models.ImageField(default='uploads/canette_coca.jpeg', upload_to='static/uploads/'),
        ),
    ]
