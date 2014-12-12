# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0004_auto_20141212_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tripentry',
            old_name='trip_entry_desc',
            new_name='entry_desc',
        ),
    ]
