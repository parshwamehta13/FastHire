# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_recruiter_recruiter_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruiter',
            name='companies_allowed',
        ),
        migrations.DeleteModel(
            name='Recruiter',
        ),
    ]
