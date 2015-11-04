# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_auto_20151104_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='hue',
            field=models.IntegerField(default=-1),
        ),
    ]
