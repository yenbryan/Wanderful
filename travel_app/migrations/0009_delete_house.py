# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0008_auto_20140919_0744'),
    ]

    operations = [
        migrations.DeleteModel(
            name='House',
        ),
    ]
