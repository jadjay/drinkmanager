# Generated by Django 3.2.7 on 2021-10-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0007_auto_20180425_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='photo',
            field=models.ImageField(default='uploads/canette.jpg', upload_to='uploads/'),
        ),
    ]