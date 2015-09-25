# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20150917_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'DEFAULT', max_length=30)),
                ('area', models.CharField(default=b'DEFAULT', max_length=30)),
                ('companies_allowed', models.ForeignKey(to='companies.Company')),
            ],
        ),
    ]
