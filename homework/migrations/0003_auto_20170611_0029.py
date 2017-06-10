# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_auto_20170609_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='estimated_date',
        ),
        migrations.AddField(
            model_name='post',
            name='desc',
            field=models.TextField(max_length=200, default=datetime.datetime(2017, 6, 10, 22, 29, 58, 620532, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
