# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 23:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20170418_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParsedLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.CharField(max_length=39)),
                ('rfc_id', models.CharField(max_length=39)),
                ('user_id', models.CharField(max_length=39)),
                ('date_time', models.CharField(max_length=29)),
                ('request_line', models.TextField()),
                ('http_status', models.CharField(max_length=3)),
                ('num_bytes', models.IntegerField(blank=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='log',
            name='log_owner',
        ),
        migrations.DeleteModel(
            name='Log',
        ),
    ]
