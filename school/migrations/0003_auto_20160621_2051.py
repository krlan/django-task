# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_school_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='img',
            field=models.URLField(verbose_name='Image URL'),
        ),
    ]
