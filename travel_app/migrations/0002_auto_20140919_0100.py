# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='location',
            field=models.ManyToManyField(related_name=b'lists', null=True, to=b'travel_app.Location'),
        ),
    ]
