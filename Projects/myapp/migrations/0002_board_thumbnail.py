# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import myapp.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='thumbnail',
            field=models.FileField(default=datetime.datetime(2018, 6, 17, 14, 46, 53, 951000, tzinfo=utc), upload_to=myapp.models.get_upload_file_name),
            preserve_default=False,
        ),
    ]
