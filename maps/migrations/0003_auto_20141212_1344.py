# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_tripentry_entry date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripentry',
            name='Entry Date',
            field=models.DateTimeField(default=b'1900-01-01 00:00:00.000000+0000'),
            preserve_default=True,
        ),
    ]
