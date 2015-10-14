# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='luminosity',
            new_name='hue',
        ),
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='event',
            name='eventfulID',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='path',
        ),
        migrations.AddField(
            model_name='event',
            name='date_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='date_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='id_source',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='source',
            field=models.CharField(null=True, max_length=2),
        ),
    ]
