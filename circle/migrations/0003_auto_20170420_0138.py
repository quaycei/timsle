# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0002_remove_circle_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('related_tag', models.ManyToManyField(blank=True, default=None, related_name='_tag_related_tag_+', to='circle.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='circle',
            name='tag',
            field=models.ManyToManyField(blank=True, default=None, to='circle.Tag'),
        ),
    ]