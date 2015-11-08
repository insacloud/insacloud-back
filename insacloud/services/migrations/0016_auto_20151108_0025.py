# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import services.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0015_auto_20151104_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='id_source',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=models.ImageField(upload_to='/home/vagrant/insacloud/insacloud/media/', validators=[services.models.validate_image_extension]),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='mosaic',
            name='image',
            field=models.ImageField(upload_to='/home/vagrant/insacloud/insacloud/media/', validators=[services.models.validate_image_extension]),
        ),
    ]
