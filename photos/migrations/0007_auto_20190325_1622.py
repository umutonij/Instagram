# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-25 13:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_auto_20190325_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='tags',
            new_name='profile',
        ),
    ]
