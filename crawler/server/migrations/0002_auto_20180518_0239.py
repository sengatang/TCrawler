# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-18 02:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HostCondig',
            new_name='HostConfig',
        ),
    ]