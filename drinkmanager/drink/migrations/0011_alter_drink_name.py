# Generated by Django 3.2.8 on 2021-10-11 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0010_alter_drink_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='name',
            field=models.CharField(default='boisson', max_length=40),
        ),
    ]
