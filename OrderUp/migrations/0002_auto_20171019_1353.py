# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-19 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderUp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='resturant',
        ),
        migrations.AddField(
            model_name='resturant',
            name='category',
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AddField(
            model_name='resturant',
            name='menu',
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AddField(
            model_name='resturant',
            name='myaddress',
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AddField(
            model_name='resturant',
            name='name',
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AddField(
            model_name='resturant',
            name='phone',
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AddField(
            model_name='resturant',
            name='price',
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]