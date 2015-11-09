# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import services.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('id_source', models.CharField(max_length=255, unique=True)),
                ('source', models.CharField(max_length=255, null=True)),
                ('date_start', models.DateTimeField(null=True)),
                ('date_end', models.DateTimeField(null=True)),
                ('category', models.TextField(null=True)),
                ('title', models.TextField()),
                ('location', models.TextField(null=True)),
                ('venue', models.TextField(null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('poster', models.ImageField(validators=[services.models.validate_image_extension], upload_to='/home/vagrant/insacloud/insacloud/media/')),
            ],
        ),
        migrations.CreateModel(
            name='Mosaic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('row', models.IntegerField(null=True)),
                ('column', models.IntegerField(null=True)),
                ('image', models.ImageField(validators=[services.models.validate_image_extension], upload_to='/home/vagrant/insacloud/insacloud/media/')),
                ('event', models.ForeignKey(to='services.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('hue', models.IntegerField(default=-1)),
                ('image', models.ImageField(upload_to='/home/vagrant/insacloud/insacloud/media/', null=True)),
                ('event', models.ForeignKey(to='services.Event')),
            ],
        ),
    ]
