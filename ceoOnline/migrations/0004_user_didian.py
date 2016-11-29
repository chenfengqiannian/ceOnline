# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceoOnline', '0003_tb_prov_city_area_street'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='didian',
            field=models.ForeignKey(blank=True, to='ceoOnline.tb_prov_city_area_street', null=True),
        ),
    ]
