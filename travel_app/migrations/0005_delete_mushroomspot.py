# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0004_mushroomspot'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MushroomSpot',
        ),
    ]
