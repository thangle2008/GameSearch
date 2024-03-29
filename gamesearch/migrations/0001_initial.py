# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('api_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('summary', models.TextField()),
                ('description', models.TextField()),
                ('score', models.FloatField(default=0)),
                ('n_reviews', models.IntegerField(default=0)),
                ('cover_img', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('api_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(to='gamesearch.Genre'),
        ),
    ]
