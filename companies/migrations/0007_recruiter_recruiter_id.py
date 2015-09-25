# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_auto_20150917_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiter',
            name='recruiter_id',
            field=models.IntegerField(default=0),
        ),
    ]
