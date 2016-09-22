# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identify', models.CharField(max_length=200, verbose_name=b'\xe7\xbb\x91\xe5\xae\x9a\xe5\x9f\x9f\xe5\x90\x8d')),
                ('exp_date', models.DateField(verbose_name=b'\xe5\x88\xb0\xe6\x9c\x9f\xe6\x97\xa5\xe6\x9c\x9f')),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u7ba1\u7406',
                'verbose_name_plural': '\u4e1a\u52a1\u7ba1\u7406',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('com_name', models.CharField(max_length=100, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0')),
                ('con_name', models.CharField(max_length=20, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d')),
                ('tel', models.CharField(max_length=20, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe7\x94\xb5\xe8\xaf\x9d')),
                ('email', models.EmailField(max_length=75, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
            ],
            options={
                'verbose_name': '\u5ba2\u6237\u7ba1\u7406',
                'verbose_name_plural': '\u5ba2\u6237\u7ba1\u7406',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dep_name', models.CharField(max_length=50, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name': '\u90e8\u95e8\u7ba1\u7406',
                'verbose_name_plural': '\u90e8\u95e8\u7ba1\u7406',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pro_name', models.CharField(max_length=50, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0')),
                ('price', models.DecimalField(verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=7, decimal_places=2)),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u7ba1\u7406',
                'verbose_name_plural': '\u4ea7\u54c1\u7ba1\u7406',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='customer',
            name='dep_name',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe9\x83\xa8\xe9\x97\xa8', to='app.Department'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='business',
            name='com_name',
            field=models.ForeignKey(verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0', to='app.Customer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='business',
            name='pro_name',
            field=models.ForeignKey(verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0', to='app.Product'),
            preserve_default=True,
        ),
    ]
