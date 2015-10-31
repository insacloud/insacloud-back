# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20151020_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='http://localhost:8080/static/', null=True),
        ),
    ]
