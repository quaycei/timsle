# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 02:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0006_auto_20170319_0217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='content',
        ),
        migrations.RemoveField(
            model_name='question',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='guideline',
            name='question',
        ),
        migrations.AddField(
            model_name='guideline',
            name='content',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='circle.Content'),
        ),
        migrations.AlterField(
            model_name='guideline',
            name='type_of_guideline',
            field=models.IntegerField(choices=[(0, 'Example'), (1, 'Rule')], default=0),
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
