# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'DEFAULT VALUE', max_length=30)),
                ('job_title', models.CharField(default=b'DEFAULT VALUE', max_length=30)),
                ('comapany_profile', models.CharField(default=b'DEFAULT VALUE', max_length=200)),
                ('job_profile', models.CharField(default=b'DEFAULT VALUE', max_length=200)),
                ('job_requirements', models.CharField(default=b'DEFAULT VALUE', max_length=200)),
                ('location', models.CharField(default=b'DEFAULT VALUE', max_length=60)),
                ('vacancies', models.IntegerField(default=0)),
                ('salary', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_applicant', models.CharField(max_length=30)),
                ('cv_applicant', models.CharField(max_length=200)),
                ('status_application', models.CharField(max_length=30)),
                ('recruiter_id', models.IntegerField(default=1)),
                ('company_applied', models.ForeignKey(to='companies.Company')),
            ],
        ),
    ]
