# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.IntegerField(default=0, choices=[(0, '\u8bf7\u6c42'), (1, '\u597d\u53cb')])),
                ('createtime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.TextField(verbose_name='\u5185\u5bb9')),
                ('createtime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u540d\u79f0')),
                ('value', models.TextField(verbose_name='\u5185\u5bb9')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=255, verbose_name='\u624b\u673a\u53f7')),
                ('password', models.CharField(max_length=255, verbose_name='\u5bc6\u7801')),
                ('jianjie', models.TextField(verbose_name='\u7b80\u4ecb')),
                ('zhiwu', models.CharField(max_length=255, verbose_name='\u804c\u52a1', blank=True)),
                ('touxiang', models.ImageField(upload_to=b'', verbose_name='\u5934\u50cf', blank=True)),
                ('image1', models.ImageField(upload_to=b'', verbose_name='\u56fe\u50cf1', blank=True)),
                ('image2', models.ImageField(upload_to=b'', verbose_name='\u56fe\u50cf2', blank=True)),
                ('image3', models.ImageField(upload_to=b'', verbose_name='\u56fe\u50cf3', blank=True)),
                ('image4', models.ImageField(upload_to=b'', verbose_name='\u56fe\u50cf4', blank=True)),
                ('image5', models.ImageField(upload_to=b'', verbose_name='\u56fe\u50cf5', blank=True)),
                ('isVIP', models.BooleanField(verbose_name='\u662f\u5426\u91d1\u8272\u540d\u79f0')),
                ('onlinetime', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='fromuser',
            field=models.ForeignKey(related_name='renews_from', to='ceoOnline.user'),
        ),
        migrations.AddField(
            model_name='news',
            name='touser',
            field=models.ForeignKey(related_name='renews_to', to='ceoOnline.user'),
        ),
        migrations.AddField(
            model_name='friend',
            name='fromuser',
            field=models.ForeignKey(related_name='refriend_from', to='ceoOnline.user'),
        ),
        migrations.AddField(
            model_name='friend',
            name='touser',
            field=models.ForeignKey(related_name='refriend_to', to='ceoOnline.user'),
        ),
    ]
