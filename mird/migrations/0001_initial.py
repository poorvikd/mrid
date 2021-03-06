# Generated by Django 3.0.1 on 2020-10-31 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('game_code', models.CharField(default='H120QZPKL', max_length=30)),
                ('video', models.URLField()),
                ('pet_name', models.CharField(max_length=20)),
            ],
        ),
    ]
