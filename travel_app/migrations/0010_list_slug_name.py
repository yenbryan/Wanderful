# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0009_delete_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='slug_name',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
