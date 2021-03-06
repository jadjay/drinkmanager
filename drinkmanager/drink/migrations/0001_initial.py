# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 12:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.DateField(max_length=40)),
                ('description', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drink.Drink')),
            ],
        ),
        migrations.AddField(
            model_name='consumption',
            name='drink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drink.Drink'),
        ),
        migrations.AddField(
            model_name='consumption',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
