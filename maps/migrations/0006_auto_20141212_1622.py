# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0005_auto_20141212_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripentry',
            name='Entry Time',
            field=models.TimeField(default=datetime.datetime(2014, 12, 12, 16, 22, 45, 869734, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tripentry',
            name='Entry Date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
