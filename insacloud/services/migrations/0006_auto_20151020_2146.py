# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20151020_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=models.ImageField(upload_to='/home/vagrant/insacloud/insacloud/media/pictures/'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='/home/vagrant/insacloud/insacloud/media/pictures/', null=True),
        ),
    ]
