# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_auto_20141212_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=200)),
                ('location_desc', models.CharField(max_length=500)),
                ('latitude', models.DecimalField(max_digits=6, decimal_places=3)),
                ('longitude', models.DecimalField(max_digits=6, decimal_places=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='tripentry',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='tripentry',
            name='longitude',
        ),
        migrations.AddField(
            model_name='tripentry',
            name='entry_locaiton',
            field=models.ForeignKey(default=1, to='maps.Location'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tripentry',
            name='Entry Date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
