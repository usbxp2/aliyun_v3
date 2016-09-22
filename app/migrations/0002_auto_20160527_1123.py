# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='host_name',
            field=models.CharField(default=b'null', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe4\xbb\xb7\xe6\xa0\xbc(\xe5\x85\x83/\xe5\xb9\xb4)', max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
    ]
