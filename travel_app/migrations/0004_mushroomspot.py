# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0003_auto_20140919_0301'),
    ]

    operations = [
        migrations.CreateModel(
            name='MushroomSpot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('geom', djgeojson.fields.PointField(default=__builtin__.dict)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
