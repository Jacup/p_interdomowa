# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_auto_20170611_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(default=datetime.datetime(2017, 6, 11, 4, 52, 38, 656090, tzinfo=utc), upload_to=''),
            preserve_default=False,
        ),
    ]
