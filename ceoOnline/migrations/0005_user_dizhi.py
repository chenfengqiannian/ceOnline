# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceoOnline', '0004_user_didian'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dizhi',
            field=models.CharField(max_length=255, verbose_name='\u5730\u5740', blank=True),
        ),
    ]
