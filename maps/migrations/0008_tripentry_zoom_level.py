# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0007_auto_20141212_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripentry',
            name='zoom_level',
            field=models.IntegerField(default=8),
            preserve_default=True,
        ),
    ]
