# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-12 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='分类名')),
                ('difficulty', models.IntegerField(choices=[(3, '高'), (2, '中'), (1, '低')], default=2, verbose_name='难度')),
                ('important_degree', models.IntegerField(choices=[(3, '高'), (2, '中'), (1, '低')], default=2, verbose_name='重要程度')),
                ('memo', models.CharField(max_length=128, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateField(verbose_name='日期')),
                ('content', models.TextField(verbose_name='日报内容')),
                ('status', models.IntegerField(choices=[(0, '可修改'), (1, '已提交'), (2, '已锁定')], default=0, verbose_name='日报状态')),
                ('hours', models.FloatField(default=7.5, verbose_name='工作时间')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='评语')),
                ('categories', models.ManyToManyField(related_name='my_categories', to='daily.Categories', verbose_name='日报分类')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile', verbose_name='所属用户')),
            ],
            options={
                'ordering': ['-upload_date', 'user'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='daily',
            unique_together=set([('upload_date', 'user')]),
        ),
    ]
