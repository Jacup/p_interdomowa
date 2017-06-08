# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='published_date',
        ),
        migrations.AddField(
            model_name='post',
            name='estimated_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
