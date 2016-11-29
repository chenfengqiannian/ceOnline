# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceoOnline', '0005_user_dizhi'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='yidu',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='yidu',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u540d\u79f0', blank=True),
        ),
    ]
