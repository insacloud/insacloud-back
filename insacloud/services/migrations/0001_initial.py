# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('eventfulID', models.IntegerField()),
                ('date', models.DateField()),
                ('duration', models.DurationField()),
                ('category', models.TextField()),
                ('title', models.TextField()),
                ('location', models.TextField()),
                ('venue', models.TextField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('poster', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Mosaic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('event', models.ForeignKey(to='services.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Mosaic_cell',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('row', models.IntegerField()),
                ('column', models.IntegerField()),
                ('mosaic', models.ForeignKey(to='services.Mosaic')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('path', models.ImageField(upload_to='')),
                ('luminosity', models.IntegerField()),
                ('event', models.ForeignKey(to='services.Event')),
            ],
        ),
        migrations.AddField(
            model_name='mosaic_cell',
            name='picture',
            field=models.ForeignKey(to='services.Picture'),
        ),
    ]
