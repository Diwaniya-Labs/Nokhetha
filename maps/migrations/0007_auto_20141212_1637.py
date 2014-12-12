# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0006_auto_20141212_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tripentry',
            old_name='Entry Time',
            new_name='entry_time',
        ),
        migrations.RemoveField(
            model_name='tripentry',
            name='Entry Date',
        ),
        migrations.AddField(
            model_name='tripentry',
            name='entry_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name=b'Date', blank=True),
            preserve_default=True,
        ),
    ]
