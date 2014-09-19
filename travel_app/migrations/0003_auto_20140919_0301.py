# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0002_auto_20140919_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='location',
            field=models.ManyToManyField(related_name=b'lists', null=True, to=b'travel_app.Location', blank=True),
        ),
    ]
