# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceoOnline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bankuai',
            field=models.CharField(max_length=255, verbose_name='\u677f\u5757', blank=True),
        ),
    ]
