# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_recruiter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruiter',
            name='companies_allowed',
        ),
        migrations.AddField(
            model_name='recruiter',
            name='companies_allowed',
            field=models.ManyToManyField(to='companies.Company'),
        ),
    ]
