# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import services.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_auto_20151108_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=models.ImageField(validators=[services.models.validate_image_extension], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='mosaic',
            name='image',
            field=models.ImageField(validators=[services.models.validate_image_extension], upload_to='media/'),
        ),
    ]
