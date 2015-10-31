# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_auto_20151028_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id_source',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='source',
            field=models.CharField(null=True, max_length=255),
        ),
    ]
