# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceoOnline', '0007_auto_20161129_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='isVIP',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u91d1\u8272\u540d\u79f0'),
        ),
    ]
