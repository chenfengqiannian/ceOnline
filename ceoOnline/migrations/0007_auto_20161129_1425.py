# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceoOnline', '0006_auto_20161129_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='value',
            new_name='neirong',
        ),
    ]
