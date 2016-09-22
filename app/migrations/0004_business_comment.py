# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='comment',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8'),
            preserve_default=True,
        ),
    ]
