# Generated by Django 3.0.1 on 2020-11-01 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mird', '0002_auto_20201031_0410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='pet_name',
        ),
    ]