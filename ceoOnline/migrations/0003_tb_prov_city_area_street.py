# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceoOnline', '0002_user_bankuai'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_prov_city_area_street',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(blank=True)),
                ('parentId', models.IntegerField(blank=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('level', models.IntegerField(blank=True)),
            ],
        ),
    ]
