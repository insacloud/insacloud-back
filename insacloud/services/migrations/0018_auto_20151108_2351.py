# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import services.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_auto_20151108_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=models.ImageField(upload_to='/home/vagrant/insacloud/insacloud/media/', validators=[services.models.validate_image_extension]),
        ),
        migrations.AlterField(
            model_name='mosaic',
            name='image',
            field=models.ImageField(upload_to='/home/vagrant/insacloud/insacloud/media/', validators=[services.models.validate_image_extension]),
        ),
    ]
