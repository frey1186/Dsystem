# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-12 15:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_articles_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='author',
        ),
    ]
