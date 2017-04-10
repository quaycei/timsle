# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0002_circle_directional_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='rank',
            field=models.IntegerField(choices=[(0, 'Enterprise'), (1, 'Station'), (2, 'Probe'), (3, 'Lander'), (4, 'Mothership')], default=0),
        ),
        migrations.AlterField(
            model_name='guideline',
            name='rank',
            field=models.IntegerField(choices=[(0, 'Enterprise'), (1, 'Station'), (2, 'Probe'), (3, 'Lander'), (4, 'Mothership')], default=3),
        ),
    ]