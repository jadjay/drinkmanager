# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2021-10-11 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0006_auto_20160112_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='photo',
            field=models.ImageField(default='static/uploads/canette.jpg', upload_to='static/uploads/'),
        ),
    ]