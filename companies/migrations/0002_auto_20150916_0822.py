# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='comapany_profile',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='cv_applicant',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='status_application',
        ),
        migrations.AddField(
            model_name='company',
            name='work_exp',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=200),
        ),
        migrations.AddField(
            model_name='resume',
            name='current_company',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=30),
        ),
        migrations.AddField(
            model_name='resume',
            name='current_salary',
            field=models.CharField(default=b'DEFAUL', max_length=10),
        ),
        migrations.AddField(
            model_name='resume',
            name='emailid',
            field=models.EmailField(default=b'DEFAULT VALUE', max_length=30),
        ),
        migrations.AddField(
            model_name='resume',
            name='mobile',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resume',
            name='position_applied',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=30),
        ),
        migrations.AddField(
            model_name='resume',
            name='resume',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=30),
        ),
        migrations.AlterField(
            model_name='company',
            name='job_profile',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=1000),
        ),
        migrations.AlterField(
            model_name='company',
            name='job_requirements',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=1000),
        ),
        migrations.AlterField(
            model_name='resume',
            name='name_applicant',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=30),
        ),
        migrations.AlterField(
            model_name='resume',
            name='recruiter_id',
            field=models.IntegerField(default=0),
        ),
    ]
