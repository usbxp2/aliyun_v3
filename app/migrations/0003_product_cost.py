# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160527_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.DecimalField(default=0, verbose_name=b'\xe6\x88\x90\xe6\x9c\xac(\xe5\x85\x83/\xe5\xb9\xb4)', max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
    ]
