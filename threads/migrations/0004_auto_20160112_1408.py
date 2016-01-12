# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0003_auto_20160111_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='comment',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 12, 14, 8, 3, 227576, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 12, 14, 8, 3, 225930, tzinfo=utc)),
        ),
    ]
