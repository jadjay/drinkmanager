# Generated by Django 3.2.8 on 2021-10-11 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0011_alter_drink_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='ean13',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='drink',
            name='name',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]