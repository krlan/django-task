# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 15:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(0)], verbose_name='Classroom number')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['-number'],
                'verbose_name_plural': 'Classrooms',
                'verbose_name': 'Classroom',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='School name')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name_plural': 'Schools',
                'verbose_name': 'School',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Full name')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Classroom')),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name_plural': 'Students',
                'verbose_name': 'Student',
            },
        ),
        migrations.AddField(
            model_name='classroom',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School'),
        ),
    ]
