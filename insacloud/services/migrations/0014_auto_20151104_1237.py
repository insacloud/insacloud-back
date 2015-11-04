# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_auto_20151103_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mosaic_cell',
            name='mosaic',
        ),
        migrations.RemoveField(
            model_name='mosaic_cell',
            name='picture',
        ),
        migrations.AddField(
            model_name='mosaic',
            name='column',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mosaic',
            name='image',
            field=models.ImageField(default='test.jpg', upload_to='/home/vagrant/insacloud/insacloud/media/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mosaic',
            name='level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mosaic',
            name='row',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Mosaic_cell',
        ),
    ]
