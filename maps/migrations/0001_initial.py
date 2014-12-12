# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nokhetha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nokhetha_name', models.CharField(max_length=200)),
                ('nokhetha_desc', models.CharField(max_length=500)),
                ('active_year_from', models.IntegerField()),
                ('active_year_to', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trip_name', models.CharField(max_length=200)),
                ('trip_desc', models.CharField(max_length=500)),
                ('nokhetha', models.ForeignKey(to='maps.Nokhetha')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TripEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trip_entry_desc', models.CharField(max_length=500)),
                ('latitude', models.DecimalField(max_digits=6, decimal_places=3)),
                ('longitude', models.DecimalField(max_digits=6, decimal_places=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_entries',
            field=models.ManyToManyField(to='maps.TripEntry'),
            preserve_default=True,
        ),
    ]
