# Generated by Django 3.0.1 on 2020-11-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mird', '0003_remove_video_pet_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='last_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
